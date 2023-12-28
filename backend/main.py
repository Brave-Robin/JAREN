import psycopg2
from fastapi import FastAPI


app = FastAPI()

conn = psycopg2.connect(
    "host=127.0.0.1 "
    "port=5432 "
    "dbname=todo "
    "user=postgres "
    "password=mysecretpassword "
    "target_session_attrs=read-write"
)
cur = conn.cursor()


def get_all_notes(count=5):
    data = cur.execute(f"select id,text,due_date,blocked_by,user_id from todo_germych limit {count};").fechall()
    return data


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return get_all_notes()
