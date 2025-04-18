CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255),
    password VARCHAR(255),
    created_at DATE
);