# Pokemon OpenAPI Example

This project contains a first OpenAPI spec you can use to generate server stubs.

## Files

- `openapi.yaml`: OpenAPI 3.0.3 spec for Pokemon CRUD routes.

## Prerequisites

- For `npx @openapitools/openapi-generator-cli ...`:
  - Java runtime installed (JRE/JDK, version 11+ recommended)
  - Internet access (first run downloads generator JARs)
- For Docker usage:
  - Docker installed and running
  - Internet access (to pull `openapitools/openapi-generator-cli`)

Install Java quickly on macOS (Homebrew):

```bash
brew install openjdk
```

Then make sure that shell can find it
```
echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
java -version
```

## 1) Validate the spec (optional but recommended)

Using Node package:

```bash
npx @openapitools/openapi-generator-cli validate -i openapi.yaml
```

Using Docker:

```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli validate -i /local/openapi.yaml
```

## 2) List available generators

```bash
npx @openapitools/openapi-generator-cli list
```

## 3) Generate server code (multiple options)

### Node.js + Express server stub

```bash
npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g nodejs-express-server \
  -o generated/nodejs-express \
  --additional-properties=usePromises=true
```

### Spring Boot server stub (Java)

```bash
npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g spring \
  -o generated/spring \
  --additional-properties=interfaceOnly=true,useSpringBoot3=true
```

### Python Flask server stub

```bash
npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g python-flask \
  -o generated/python-flask
```

### Go server stub

```bash
npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g go-server \
  -o generated/go-server \
  --additional-properties=router=chi
```

## 4) Useful generate flags to experiment with

- `--skip-validate-spec`: skip validation step.
- `--global-property=apis,models`: limit generated outputs.
- `--additional-properties=key=value,key2=value2`: generator-specific options.
- `--package-name=my_api`: set package/module name for some generators.
- `--git-user-id` and `--git-repo-id`: embed metadata in generated projects.

## 5) Example using Docker instead of npx

```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i /local/openapi.yaml \
  -g spring \
  -o /local/generated/spring-docker \
  --additional-properties=interfaceOnly=true,useSpringBoot3=true
```
