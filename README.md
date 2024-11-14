# FastAPI Starter

## Quickstart

Bring up postgres:
```bash
$ docker compose up -d
```

Install dependencies and bring up a FastAPI server
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

# API

Let's work off of this [document](https://judicious-dinner-b5d.notion.site/Data-to-API-1181df5314338020b796ed5f5f10ae9d).
