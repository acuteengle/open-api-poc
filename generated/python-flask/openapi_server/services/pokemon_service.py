from datetime import datetime, timezone
from uuid import uuid4


# In-memory store for learning/demo purposes.
# Replace this with your database/repository layer.
_POKEMON_STORE = {}


def _now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _error(message, status):
    return {"message": message}, status


def _coerce_input(raw):
    if raw is None:
        return {}
    if isinstance(raw, dict):
        return raw
    if hasattr(raw, "to_dict"):
        return raw.to_dict()
    return {}


def _normalize_create_input(raw):
    data = _coerce_input(raw)
    name = data.get("name")
    ptype = data.get("type")
    level = data.get("level")
    is_legendary = data.get("isLegendary", data.get("is_legendary", False))

    if not name or not ptype or level is None:
        raise ValueError("name, type, and level are required.")

    try:
        parsed_level = int(level)
    except (TypeError, ValueError):
        raise ValueError("level must be an integer between 1 and 100.")

    if parsed_level < 1 or parsed_level > 100:
        raise ValueError("level must be an integer between 1 and 100.")

    return {
        "name": str(name).strip(),
        "type": str(ptype).strip().lower(),
        "level": parsed_level,
        "isLegendary": bool(is_legendary),
    }


def _get_or_404(pokemon_id):
    pokemon = _POKEMON_STORE.get(pokemon_id)
    if pokemon is None:
        return None, _error("Pokemon not found.", 404)
    return pokemon, None


def _apply_partial_update(existing, raw):
    payload = _coerce_input(raw)
    if len(payload.keys()) < 1:
        raise ValueError("At least one field must be provided for update.")

    allowed = {"name", "type", "level", "isLegendary", "is_legendary"}
    unknown_fields = set(payload.keys()) - allowed
    if unknown_fields:
        raise ValueError(f"Unsupported field: {next(iter(unknown_fields))}")

    updated = dict(existing)
    if "name" in payload:
        updated["name"] = str(payload["name"]).strip()
    if "type" in payload:
        updated["type"] = str(payload["type"]).strip().lower()
    if "level" in payload:
        try:
            parsed_level = int(payload["level"])
        except (TypeError, ValueError):
            raise ValueError("level must be an integer between 1 and 100.")
        if parsed_level < 1 or parsed_level > 100:
            raise ValueError("level must be an integer between 1 and 100.")
        updated["level"] = parsed_level
    if "isLegendary" in payload:
        updated["isLegendary"] = bool(payload["isLegendary"])
    if "is_legendary" in payload:
        updated["isLegendary"] = bool(payload["is_legendary"])

    updated["updatedAt"] = _now_iso()
    return updated


def create_pokemon(pokemon_create_request):
    try:
        normalized = _normalize_create_input(pokemon_create_request)
    except ValueError as exc:
        return _error(str(exc), 400)

    now = _now_iso()
    new_pokemon = {
        "id": str(uuid4()),
        **normalized,
        "createdAt": now,
        "updatedAt": now,
    }
    _POKEMON_STORE[new_pokemon["id"]] = new_pokemon
    return new_pokemon, 201


def delete_pokemon_by_id(pokemon_id):
    _, not_found = _get_or_404(pokemon_id)
    if not_found:
        return not_found
    del _POKEMON_STORE[pokemon_id]
    return "", 204


def get_pokemon_by_id(pokemon_id):
    pokemon, not_found = _get_or_404(pokemon_id)
    if not_found:
        return not_found
    return pokemon, 200


def list_pokemon(limit=None, offset=None):
    parsed_limit = 20 if limit is None else limit
    parsed_offset = 0 if offset is None else offset

    try:
        parsed_limit = int(parsed_limit)
        parsed_offset = int(parsed_offset)
    except (TypeError, ValueError):
        return _error("limit and offset must be integers.", 400)

    if parsed_limit < 1:
        return _error("limit must be an integer >= 1.", 400)
    if parsed_offset < 0:
        return _error("offset must be an integer >= 0.", 400)

    all_items = list(_POKEMON_STORE.values())
    items = all_items[parsed_offset: parsed_offset + parsed_limit]
    return {
        "items": items,
        "total": len(all_items),
        "limit": parsed_limit,
        "offset": parsed_offset,
    }, 200


def replace_pokemon_by_id(pokemon_id, pokemon_create_request):
    existing, not_found = _get_or_404(pokemon_id)
    if not_found:
        return not_found

    try:
        normalized = _normalize_create_input(pokemon_create_request)
    except ValueError as exc:
        return _error(str(exc), 400)

    replaced = {
        "id": existing["id"],
        **normalized,
        "createdAt": existing["createdAt"],
        "updatedAt": _now_iso(),
    }
    _POKEMON_STORE[pokemon_id] = replaced
    return replaced, 200


def update_pokemon_by_id(pokemon_id, pokemon_update_request):
    existing, not_found = _get_or_404(pokemon_id)
    if not_found:
        return not_found

    try:
        updated = _apply_partial_update(existing, pokemon_update_request)
    except ValueError as exc:
        return _error(str(exc), 400)

    _POKEMON_STORE[pokemon_id] = updated
    return updated, 200
