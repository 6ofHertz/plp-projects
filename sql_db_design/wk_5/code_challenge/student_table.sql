CREATE TABLE student (
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

CREATE INDEX IdxAge ON student(age);
