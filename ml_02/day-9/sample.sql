-- sample.sql: creates a table, inserts rows, and selects them
CREATE TABLE IF NOT EXISTS sample_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);

INSERT INTO sample_table (name, age) VALUES ('Alice', 30);
INSERT INTO sample_table (name, age) VALUES ('Bob', 25);
INSERT INTO sample_table (name, age) VALUES ('Carol', 28);

-- Query to show inserted rows
SELECT id, name, age FROM sample_table;
