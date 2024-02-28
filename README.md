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
