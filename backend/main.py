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
    cur.execute(f"select id, text, due_date, blocked_by, user_id from todos limit {count}")
    data = cur.fetchall()
    return data


def get_minimal_available_id():
    cur.execute('SELECT MAX(id) FROM todos')
    minimal_id = cur.fetchone()[0]
    return minimal_id + 1


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return get_all_notes()


"""
add column status. Execute in dbeaver

--ALTER TABLE todos
--ADD todo_status boolean NOT NULL DEFAULT False;

"""