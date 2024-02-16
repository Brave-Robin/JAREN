INSERT INTO todos (todo_text,todo_due_date,todo_blocked_by,todo_status,todo_user_id) VALUES
	 ('купить жильё','2024-12-30',0,false,1000),
	 ('Получить L3','2024-12-30',0,false,1000),
	 ('Поднять английский до B2/B2+','2024-12-30',0,false,1000),
	 ('Сертификаты','2024-12-30',0,false,1000),
	 ('Изучить Грузинский до A2','2024-12-30',0,false,1000),
	 ('Получить права A/B','2024-12-30',0,false,1000),
	 ('Купить велосипед','2024-12-30',0,false,1000),
     ('Neuvěřitelně propracovaný model závodního Ferrari šokuje detaily, ale také cenou. Stojí jako nová Fabia','2024-01-01',NULL,false,1001),
	 ('Моды для КСП',NULL,NULL,false,1001),
	 ('Bannerlord Skill Cap Formula',NULL,NULL,false,1001),
	 ('Лучшие юниты в Bannerlord',NULL,NULL,false,1001),
	 ('Пехота: стургийский ратник',NULL,4,false,1001),
	 ('Марк_Лутц_Изучаем_Python_5_издание__том_1_2019.pdf','2024-01-12',NULL,false,1001),
	 ('Марк_Лутц_Изучаем_Python_5_издание__том_1_2019.pdf','2024-01-12',NULL,false,1001),
	 ('Марк_Лутц_Изучаем_Python_5_издание__том_1_2019.pdf','2024-01-12',NULL,false,1001),
	 ('Моды для КСП',NULL,NULL,false,1001),
	 ('some text','2025-01-15',1,true,1001),
	 ('რა არის დრო','2024-03-04',NULL,false,1002),
	 ('რა არის სივრცე','2024-05-30',NULL,true,1002),
	 ('რა არის მორალი','2025-01-01',NULL,true,1002),
	 ('რა არის საზოგადოება','2024-09-21',NULL,false,1002),
	 ('რა არის არაფერი','2026-06-06',NULL,false,1002);


--create DATABASE todo;
--drop table todos;

--CREATE TABLE todos (
--	todo_id serial PRIMARY KEY,
--	todo_text text NOT NULL,
--	todo_due_date date,
--	todo_blocked_by int,
--	todo_status boolean NOT NULL,
--	todo_user_id int NOT NULL
--	);

--insert INTO todos (text, status, blocked_by, id, user_id) values ('Create DB', false, 3, 1, 1000);

--ALTER TABLE todos ADD user_id int;
--SELECT MAX(todo_id) FROM todos;
select * from todos t;

--SELECT CURRENT_DATE;
--SELECT EXTRACT(EPOCH FROM NOW());
--SELECT EXTRACT (EPOCH FROM TIMESTAMP '2024-01-10');
--select extract( epoch from current_timestamp::timestamp with time zone at time zone 'UTC');
--select extract( EPOCH FROM TIMESTAMP '2024-01-10' with time zone at time zone 'UTC');
--select extract( epoch from current_timestamp::timestamp with time zone at time zone 'Asia/Tbilisi');

--drop TABLE todos;

--CREATE TABLE todos (
--    todo_id serial PRIMARY KEY,
--    todo_text text NOT NULL,
--    todo_due_date date,
--    todo_blocked_by int,
--    todo_status boolean NOT NULL,
--    todo_user_id int NOT NULL
--    );