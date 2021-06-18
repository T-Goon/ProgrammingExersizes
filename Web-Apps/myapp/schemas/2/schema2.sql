CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS leads (
    id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(), 
    createdOn DATE DEFAULT CURRENT_DATE, 
    updatedOn DATE DEFAULT CURRENT_DATE, 
    email TEXT);

CREATE TABLE IF NOT EXISTS users (
    id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(), 
    username TEXT,
    firstName TEXT,
    lastName TEXT,
    password TEXT,
    email TEXT UNIQUE,
    isAdmin BOOLEAN DEFAULT false);