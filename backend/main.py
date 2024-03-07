""" to_do backend part """

import psycopg2
import os

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
    todo_id: int
    todo_text: str
    todo_due_date: str | None = 'NULL'
    todo_blocked_by: int | None = 0
    todo_status: bool | None = False
    todo_user_id: int


def get_all_notes(count: int = 50) -> list:
    """
    :param count: select limit from DB
    :return: list of lists
    """
    cur.execute(
        f"select "
        f"todo_id, "
        f"todo_text, "
        f"todo_due_date, "
        f"todo_blocked_by, "
        f"todo_status, "
        f"todo_user_id "
        f"from todos limit {count}"
    )
    data = cur.fetchall()
    return data


def get_minimal_available_id() -> int:
    """
    :param: none
    :return: integer next minimal ID
    """
    cur.execute('SELECT MAX(todo_id) FROM todos')
    minimal_id = cur.fetchone()[0]
    if minimal_id is None:
        return 1
    return minimal_id + 1


def check_data(new_id, todo_text, todo_due_date, todo_blocked_by, todo_status, todo_user_id):
    cur.execute(
        f"select todo_id, "
        f"todo_text, "
        f"todo_due_date, "
        f"todo_blocked_by, "
        f"todo_status, "
        f"todo_user_id "
        f"from todos "
        f"where "
        f"todo_id = {new_id} and "
        f"todo_text = '{todo_text}' and "
        f"to_char(todo_due_date, 'YYYY-MM-DD') = '{todo_due_date}' and "
        # f"todo_blocked_by = null and "
        f"todo_status = '{todo_status}' and "
        f"todo_user_id = '{todo_user_id}';"
    )
    if len(str(cur.fetchone())) > 5:
        return True
    return False
# TODO: Fix SQL query todo_blocked_by



@app.get("/")
async def root() -> list:
    """
    :param: none
    :return: all notes
    """
    return get_all_notes()


# @app.get("/test")
# async def root():
#     return check_data()


@app.put("/create/")
async def update_item(
        todo_text: str,
        todo_due_date: str,
        todo_blocked_by: int,
        todo_status: bool,
        todo_user_id: int
):
    """
    :param todo_text:
    :param todo_due_date:
    :param todo_blocked_by:
    :param todo_status:
    :param todo_user_id:
    :return: todo_status code
    """
    new_id: int = get_minimal_available_id()
    cur.execute(
        f"INSERT INTO todos Values("
        f"{new_id}, "
        f"'{todo_text}', "
        f"'{todo_due_date}', "
        f"'{todo_blocked_by}', "
        f"'{todo_status}', "
        f"'{todo_user_id}'"
        f");"
    )
    # TODO: need return web codes 200, 500, etc. need use web-signal(WEB SERVER ERROR TYPES)
    conn.commit()
    if check_data(new_id, todo_text, todo_due_date, todo_blocked_by, todo_status, todo_user_id):
        return 200
    return 500


@app.put("/update/{todo_id}")
def update_data(
        todo_id: int,
        todo_text: str,
        todo_due_date: str,
        todo_blocked_by: int,
        todo_status: bool,
        todo_user_id: int
):
    cur.execute(
        f"UPDATE todos SET "
        f"todo_text = '{todo_text}', "
        f"todo_due_date = '{todo_due_date}', "
        f"todo_blocked_by = '{todo_blocked_by}', "
        f"todo_status = '{todo_status}', "
        f"todo_user_id = '{todo_user_id}' "
        f"WHERE todo_id = {todo_id} "
        f";"
    )
    conn.commit()
    return 200


@app.delete("/delete/{todo_id}")
def delete_data(
        todo_id: int,
):
    cur.execute(
        f"DELETE FROM todos "
        f"WHERE todo_id = {todo_id} "
        f";"
    )
    conn.commit()
    return 200


