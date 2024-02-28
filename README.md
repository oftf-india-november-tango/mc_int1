# FastAPI Starter

## Quickstart

With a Postgres DB running on port `localhost:5432`... with username/password/database of "postgres"

```bash
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ make dev
```

Then (in another shell,) curl the hello world endpoint and health endpoint
```bash
$ curl localhost:8000/
{"message":"Hello World"}

$ curl localhost:8000/health
{"pg":[1]}
```

# Data Ingestion

Let's work off of this [document](https://judicious-dinner-b5d.notion.site/Product-API-6535057372a843df93a898b013c79f9f).
