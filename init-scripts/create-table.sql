--CREATE DATABASE test1;

CREATE TABLE todo_germych (
	id serial PRIMARY KEY,
	text text NOT NULL,
	due_date date,
	blocked_by int,
	user_id int
    );
