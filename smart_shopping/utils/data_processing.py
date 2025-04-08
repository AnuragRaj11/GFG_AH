import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from database.db_manager import get_connection, create_tables

def load_user_data(csv_path='data/customer_data_collection.csv'):
    df = pd.read_csv(csv_path)
    print("Loaded User Data:\n", df.head())

    conn = get_connection()
    df.to_sql('Users', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print("User data loaded into database.")

def load_product_data(csv_path='data/product_recommendation_data.csv'):
    df = pd.read_csv(csv_path)
    print("Loaded Product Data:\n", df.head())

    conn = get_connection()
    df.to_sql('Products', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print("Product data loaded into database.")

if __name__ == '__main__':
    create_tables()
    load_user_data()
    load_product_data()
