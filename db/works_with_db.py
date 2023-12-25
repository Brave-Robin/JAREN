""" test module for DB 'how to work' """

import psycopg2

conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=postgres user=postgres password=mysecretpassword target_session_attrs=read-write")

cur = conn.cursor()


# cur.execute("CREATE TABLE todo_germych (id serial PRIMARY KEY, text text NOT NULL, due_date date, "
#             "blocked_by int, user_id int);")

# cur.execute("INSERT INTO todo_germych VALUES (new_id, 'CZ');")


def get_next_id():
    cur.execute("SELECT MAX(id) FROM todo_germych;")
    note_ids = cur.fetchall()
    return note_ids[0][0] + 1

print(get_next_id())


# cur.execute("UPDATE todo_germych SET due_date='12-21-2023' WHERE id=5;")


