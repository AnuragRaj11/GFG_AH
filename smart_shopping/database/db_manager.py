import sqlite3

DB_PATH = "smart_shopping.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            Customer_ID TEXT PRIMARY KEY,
            Gender TEXT,
            Age INTEGER,
            Location TEXT,
            Marital_Status TEXT,
            Purchase_History TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            Product_ID TEXT PRIMARY KEY,
            description TEXT,
            Category TEXT,
            Price REAL,
            Brand TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Interactions (
            interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            product_id TEXT,
            action TEXT,
            timestamp TEXT,
            FOREIGN KEY(user_id) REFERENCES Users(Customer_ID),
            FOREIGN KEY(product_id) REFERENCES Products(Product_ID)
        );
    ''')

    conn.commit()
    conn.close()
