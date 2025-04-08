import sqlite3

def get_connection():
    return sqlite3.connect("smart_shopping.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        Customer_ID INTEGER PRIMARY KEY,
        Gender TEXT,
        Age INTEGER,
        Location TEXT,
        Marital_Status TEXT,
        Purchase_History TEXT
    )
    """)

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY,
        description TEXT,
        category TEXT,
        price REAL
    )
    """)

    # User_Interactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User_Interactions (
        interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        action TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users (Customer_ID),
        FOREIGN KEY (product_id) REFERENCES Products (product_id)
    )
    """)

    conn.commit()
    conn.close()
