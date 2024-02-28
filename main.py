from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=postgres host=localhost")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    return {"pg": result}
