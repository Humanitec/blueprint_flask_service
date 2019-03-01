# Template for Flask Blueprint

Template for creating Humanitec backend service application

## Development

Build the image:

```
docker-compose build
```

Run the web server:

```
docker-compose up
```

Open your browser with URL `http://localhost:8089`.

Swagger schema URL `http://localhost:8089/docs/`.

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' flask_app_service
```
