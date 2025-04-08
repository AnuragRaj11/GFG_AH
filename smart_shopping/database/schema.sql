-- Create Users Table
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    preferences TEXT
);

-- Create Products Table
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    description TEXT,
    tags TEXT,
    availability INTEGER
);

-- Create User_Interactions Table
CREATE TABLE IF NOT EXISTS User_Interactions (
    interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER,
    timestamp TEXT,
    action TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

-- Create Recommendations Table
CREATE TABLE IF NOT EXISTS Recommendations (
    recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    recommended_products TEXT,
    timestamp TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
);
