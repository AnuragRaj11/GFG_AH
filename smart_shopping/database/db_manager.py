import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "smart_shopping.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            location TEXT
        );
    ''')

    # ✅ Create Products table with all required fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            Product_ID TEXT PRIMARY KEY,
            Category TEXT,
            Subcategory TEXT,
            Price REAL,
            Brand TEXT,
            Average_Rating_of_Similar_Products REAL,
            Product_Rating REAL,
            Customer_Review_Sentiment_Score REAL,
            Holiday TEXT,
            Season TEXT,
            Geographical_Location TEXT,
            Similar_Product_List TEXT,
            Probability_of_Recommendation REAL
        );
    ''')

    # Create User_Interactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            product_id TEXT,
            action TEXT,
            timestamp TEXT,
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (product_id) REFERENCES Products(Product_ID)
        );
    ''')

    conn.commit()
    conn.close()
