""" to_do backend part """
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


def get_all_notes(count: int = 5) -> list:
    """
    :param count: select limit from DB
    :return: list of lists
    """
    cur.execute(f"select id, text, due_date, blocked_by, user_id from todos limit {count}")
    data = cur.fetchall()
    return data


def get_minimal_available_id() -> int:
    """
    :param: none
    :return: integer next minimal ID
    """
    cur.execute('SELECT MAX(id) FROM todos')
    minimal_id = cur.fetchone()[0]
    return minimal_id + 1


@app.get("/")
async def root() -> list:
    """
    :param: none
    :return: all notes
    """
    return get_all_notes()
