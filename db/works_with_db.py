""" test module for DB 'how to work' """

import psycopg2

conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=test user=postgres password=mysecretpassword target_session_attrs=read-write")

cur = conn.cursor()

cur.execute("INSERT INTO todos VALUES (2, 'test text again');")
conn.commit()
