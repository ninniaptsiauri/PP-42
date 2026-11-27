CREATE TABLE students(
	id serial primary key,
	name varchar(30) not null,
	email varchar(50) unique not null,
	birth_date date,
	enrolled boolean default true,
	created_at timestamp default now()
)

INSERT INTO students(name, email, enrolled) VALUES('John', 'john1@gmail.com', false)

INSERT INTO students
  (id, name, email, birth_date, enrolled, created_at)
VALUES
  (DEFAULT, 'Tako Chikovani',
   'tako@example.com', '2002-03-30',
   TRUE, DEFAULT);


INSERT INTO students(name, email, enrolled) VALUES
	('Ana', 'ana@gmail.com', false),
	('Mary', 'mary@gmail.com', true),
	('Sam', 'sam@gmail.com', true),
	('Mary', 'mary1@gmail.com', true),
	('Ana', 'ana1@gmail.com', true)


SELECT * FROM students

SELECT * FROM students ORDER BY created_at desc

SELECT * FROM students LIMIT 3

SELECT name, email FROM students

SELECT name, email FROM students WHERE id = 1

SELECT * FROM students WHERE name = 'Ana'

SELECT * FROM students WHERE name = 'Ana' AND enrolled = false

SELECT * FROM students WHERE name = 'Ana' OR enrolled = false

SELECT * FROM students WHERE name LIKE 'Ana%'

SELECT * FROM students WHERE name LIKE '%na'

SELECT * FROM students WHERE name LIKE '%na%'

SELECT * FROM students WHERE name ILIKE 'ana%'

UPDATE students SET birth_date = '2000-10-22'

UPDATE students SET birth_date = '2001-07-20' WHERE id = 1

UPDATE students SET birth_date = '2001-Aug-20' WHERE id = 3

UPDATE students SET birth_date = '2001-Aug-20', enrolled = true WHERE id = 3

DELETE FROM students where id = 1

DROP TABLE students

DROP DATABASE "PP-42"

