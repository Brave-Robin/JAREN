""" test module for DB 'how to work' """

import psycopg2

conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=todo user=postgres password=mysecretpassword target_session_attrs=read-write")

cur = conn.cursor()

# zapros = cur.execute(f"SELECT id,text,due_date,blocked_by,user_id FROM todo_germych LIMIT 5;")
zapros = cur.execute("SELECT * FROM todo_germych")
print(zapros)
print(type(zapros))
# def create_note(id, text, due_date='NULL', blocked_by='NULL', user_id='NULL'):
#     cur.execute(f"INSERT INTO todo_germych Values({id}, '{text}', '{due_date}', {blocked_by}, {user_id});")
#     return conn.commit()
#
#
# create_note(8,'Марк_Лутц_Изучаем_Python_5_издание__том_1_2019.pdf', '01-12-2024', blocked_by="NULL")

# cur.execute("CREATE TABLE todo_germych (id serial PRIMARY KEY, text text NOT NULL, due_date date, "
#             "blocked_by int, user_id int);")

# cur.execute("INSERT INTO todo_germych (id, text, due_date, "
#             "blocked_by, user_id) VALUES (1, 'Neuvěřitelně propracovaný model závodního Ferrari šokuje detaily, "
#             "ale také cenou. Stojí jako nová Fabia', '01-01-2024',NULL,NULL);")


# cur.execute("INSERT INTO todo_germych (id, text, due_date, blocked_by, user_id) VALUES (25, 'Моды для КСП', NULL, "
#             "NULL, NULL);")


# cur.execute("INSERT INTO todo_germych (id, text, due_date, blocked_by, user_id) VALUES (3, 'Bannerlord Skill Cap Formula', NULL, "
#             "NULL, NULL);")


# cur.execute("INSERT INTO todo_germych (id, text, due_date, blocked_by, user_id) VALUES (4, 'Лучшие юниты в Bannerlord', NULL, "
#             "NULL, NULL);")


# cur.execute("INSERT INTO todo_germych (id, text, due_date, blocked_by, user_id) VALUES (5, 'Пехота: стургийский ратник', NULL, "
#             "4, NULL);")
#
#
# conn.commit()

# def get_next_id():
#     cur.execute("SELECT MAX(id) FROM todo_germych;")
#     note_ids = cur.fetchall()
#     return note_ids[0][0] + 1
#
# print(get_next_id())


# cur.execute("UPDATE todo_germych SET due_date='12-21-2023' WHERE id=5;")


