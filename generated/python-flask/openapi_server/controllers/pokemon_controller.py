import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.pokemon import Pokemon  # noqa: E501
from openapi_server.models.pokemon_create_request import PokemonCreateRequest  # noqa: E501
from openapi_server.models.pokemon_list_response import PokemonListResponse  # noqa: E501
from openapi_server.models.pokemon_update_request import PokemonUpdateRequest  # noqa: E501
from openapi_server import util


def create_pokemon(body):  # noqa: E501
    """Create Pokemon

     # noqa: E501

    :param pokemon_create_request: 
    :type pokemon_create_request: dict | bytes

    :rtype: Union[Pokemon, Tuple[Pokemon, int], Tuple[Pokemon, int, Dict[str, str]]
    """
    pokemon_create_request = body
    if connexion.request.is_json:
        pokemon_create_request = PokemonCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pokemon_by_id(pokemon_id):  # noqa: E501
    """Delete Pokemon by ID

     # noqa: E501

    :param pokemon_id: Unique ID of a Pokemon.
    :type pokemon_id: str
    :type pokemon_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_pokemon_by_id(pokemon_id):  # noqa: E501
    """Get Pokemon by ID

     # noqa: E501

    :param pokemon_id: Unique ID of a Pokemon.
    :type pokemon_id: str
    :type pokemon_id: str

    :rtype: Union[Pokemon, Tuple[Pokemon, int], Tuple[Pokemon, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_pokemon(limit=None, offset=None):  # noqa: E501
    """List Pokemon

     # noqa: E501

    :param limit: Maximum number of Pokemon to return.
    :type limit: int
    :param offset: Number of Pokemon to skip.
    :type offset: int

    :rtype: Union[PokemonListResponse, Tuple[PokemonListResponse, int], Tuple[PokemonListResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def replace_pokemon_by_id(pokemon_id, body):  # noqa: E501
    """Replace Pokemon by ID

     # noqa: E501

    :param pokemon_id: Unique ID of a Pokemon.
    :type pokemon_id: str
    :type pokemon_id: str
    :param pokemon_create_request: 
    :type pokemon_create_request: dict | bytes

    :rtype: Union[Pokemon, Tuple[Pokemon, int], Tuple[Pokemon, int, Dict[str, str]]
    """
    pokemon_create_request = body
    if connexion.request.is_json:
        pokemon_create_request = PokemonCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_pokemon_by_id(pokemon_id, body):  # noqa: E501
    """Update Pokemon by ID

     # noqa: E501

    :param pokemon_id: Unique ID of a Pokemon.
    :type pokemon_id: str
    :type pokemon_id: str
    :param pokemon_update_request: 
    :type pokemon_update_request: dict | bytes

    :rtype: Union[Pokemon, Tuple[Pokemon, int], Tuple[Pokemon, int, Dict[str, str]]
    """
    pokemon_update_request = body
    if connexion.request.is_json:
        pokemon_update_request = PokemonUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
