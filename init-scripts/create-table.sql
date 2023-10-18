--CREATE DATABASE test1;

CREATE TABLE todos (
	todo_id serial PRIMARY KEY,
	todo_text text NOT NULL,
	todo_due_date date,
	todo_blocked_by int
    );
