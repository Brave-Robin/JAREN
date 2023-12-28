""" test module for DB 'how to work' """

import psycopg2

conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=todo user=postgres password=mysecretpassword target_session_attrs=read-write")

cur = conn.cursor()


def get_next_id():
    cur.execute("SELECT MAX(id) FROM todos;")
    note_ids = cur.fetchall()
    return note_ids[0][0] + 1


def new_task():
    print('enter new task: ')
    task = input()
    new_id = get_next_id()
    cur.execute(f"INSERT INTO todos Values({new_id}, '{task}');")
    return conn.commit()
print(new_task())

# cur.execute("INSERT INTO todos VALUES (2, 'test text again');")
# conn.commit()
