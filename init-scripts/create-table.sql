--create DATABASE todo;

CREATE TABLE todos (
	todo_id serial PRIMARY KEY,
	todo_text text NOT NULL,
	todo_due_date date,
	todo_blocked_by int,
	todo_status boolean NOT NULL,
	todo_user_id int NOT NULL
	);