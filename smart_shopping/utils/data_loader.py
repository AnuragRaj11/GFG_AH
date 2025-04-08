import pandas as pd
import os
import streamlit as st
from database.db_manager import get_connection, create_tables

def load_user_data(path='data/customer_data_collection.csv'):
    if not os.path.exists(path):
        st.error(f"❌ Missing file: {path}")
        return
    df = pd.read_csv(path)
    conn = get_connection()
    df.to_sql('Users', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def load_product_data(path='data/product_recommendation_data.csv'):
    if not os.path.exists(path):
        st.error(f"❌ Missing file: {path}")
        return
    df = pd.read_csv(path)
    conn = get_connection()
    df.to_sql('Products', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
