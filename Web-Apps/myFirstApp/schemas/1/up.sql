CREATE TABLE IF NOT EXISTS users (
    id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(), 
    username TEXT,
    firstName TEXT,
    lastName TEXT,
    password TEXT,
    email TEXT UNIQUE);