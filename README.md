# [Module] service (Flask)

## Overview

_Please address the following points:_

-  _What does this service enable you to do with your Walhall app?_
-  _What kinds of data models does this service provide for your app?_
-  _An overview of how the data models work together._

## REST data models

### [Model 1]

A _[model 1]_ has the following properties:

-  **[Property]:** One-sentence description of the property.
-  **[Property]:** One-sentence description of the property.
-  **[Property]:** One-sentence description of the property.

#### Endpoints

-  `GET /{model1}/{property}/`: Retrieves a ____.
-  `POST /{model1}/{property}/`: Creates a ____.
-  `PATCH /{model1}/{property}/`: Updates a ____.
-  `DELETE /{model1}/{property}/`: Deletes a ____.

[Click here for the full API documentation.](#point-this-link-to-swagger-docs)

### [Model 2]

A _[model 2]_ has the following properties:

-  **[Property]:** One-sentence description of the property.
-  **[Property]:** One-sentence description of the property.
-  **[Property]:** One-sentence description of the property.

#### Endpoints

-  `GET /{model2}/{property}/`: Retrieves a ____.
-  `POST /{model2}/{property}/`: Creates a ____.
-  `PATCH /{model2}/{property}/`: Updates a ____.
-  `DELETE /{model2}/{property}/`: Deletes a ____.

[Click here for the full API documentation.](#point-this-link-to-swagger-docs)

## Non-REST endpoints

_This is a section where you would document endpoints that are not related to a data model, e.g., with the search service._

_For each of these endpoints, a more in-depth explanation is necessary._

## Local development

### Prerequisites

You must have [Docker](https://www.docker.com/) installed.

### Build & run service locally

Build the Docker image:

```bash
docker-compose build
```

Run a web server with this service:

```bash
docker-compose up
```

Now, open your browser and go to [http://localhost:8080](http://localhost:8080).

For the admin panel, go to [http://localhost:8080/admin](http://localhost:8080/admin)
(user: `admin`, password: `admin`).

### Run tests

To run the tests once:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' {name-of-service}
```

To run the tests and leave bash open inside the container so that it's possible to
re-run the tests faster again using `bash scripts/run-tests.sh [--keepdb]`:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh --bash-on-finish' {name-of-service}
```

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' {name-of-service}
```

## License

Copyright &#169;2019 Humanitec GmbH.

This code is released under the [Humanitec Affero GPL](LICENSE).
