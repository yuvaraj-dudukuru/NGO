CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
);

INSERT INTO students (name, grade) VALUES ('Alice', 95), ('Bob', 88);

SELECT * FROM students;