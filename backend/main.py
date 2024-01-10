""" to_do backend part """
import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# TODO: move settings to ENV variables (docker preparing)
conn = psycopg2.connect(
    "host=127.0.0.1 "
    "port=5432 "
    "dbname=todo "
    "user=postgres "
    "password=mysecretpassword "
    "target_session_attrs=read-write"
)
cur = conn.cursor()

"""
Example date in postgresql 2024-01-10
"""


class Item(BaseModel):
    """
    to_do validation
    """
    id: int
    text: str
    due_date: str | None = 'NULL'
    blocked_by: int | None = 0
    status: bool | None = False
    user_id: int


def get_all_notes(count: int = 10) -> list:
    """
    :param count: select limit from DB
    :return: list of lists
    """
    cur.execute(
        f"select id, text, due_date, blocked_by, status, user_id from todos limit {count}"
    )
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


@app.put("/create/")
async def update_item(text: str, due_date: str, blocked_by: int, status: bool, user_id: int):
    """
    :param text:
    :param due_date:
    :param blocked_by:
    :param status:
    :param user_id:
    :return: status code
    """
    new_id: int = get_minimal_available_id()
    cur.execute(
        f"INSERT INTO todos Values("
        f"{new_id}, "
        f"'{text}', "
        f"'{due_date}', "
        f"'{blocked_by}', "
        f"'{status}', "
        f"'{user_id}'"
        f");"
    )
    # TODO: need return web codes 200, 500, etc.
    conn.commit()
    return 200
