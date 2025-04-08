import os
import pandas as pd
import sqlite3
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DB_PATH = "smart_shopping.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User_Interactions (
            interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            product_id TEXT,
            action TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES Users(Customer_ID),
            FOREIGN KEY(product_id) REFERENCES Products(Product_ID)
        );
    ''')

    conn.commit()
    conn.close()

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

def log_interaction(user_id, product_id, action):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO User_Interactions (user_id, product_id, action)
        VALUES (?, ?, ?)
    ''', (user_id, product_id, action))
    conn.commit()
    conn.close()

def get_product_info(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE Product_ID = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

def build_recommender():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Products", conn)
    conn.close()

    # Handle missing columns gracefully
    df['description'] = (
        df.get('Category', pd.Series('')).fillna('') + ' ' +
        df.get('Subcategory', pd.Series('')).fillna('') + ' ' +
        df.get('Brand', pd.Series('')).fillna('') + ' ' +
        df.get('Season', pd.Series('')).fillna('') + ' ' +
        df.get('Geographical_Location', pd.Series('')).fillna('')
    )

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    sim_matrix = cosine_similarity(tfidf_matrix)

    return df, sim_matrix


def generate_recommendations(user_id, top_n=5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_id FROM User_Interactions
        WHERE user_id = ? ORDER BY timestamp DESC LIMIT 1
    """, (user_id,))
    last = cursor.fetchone()
    conn.close()

    if not last:
        return []

    df, sim_matrix = build_recommender()
    product_id = last[0]
    if product_id not in df['Product_ID'].values:
        return []

    idx = df.index[df['Product_ID'] == product_id][0]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    recommended_ids = [df.iloc[i[0]]['Product_ID'] for i in sim_scores]
    return recommended_ids

# Streamlit UI
st.set_page_config(page_title="Smart Shopping Recommender", layout="centered")
st.title("🛍️ Smart Shopping AI Recommender")

create_tables()
if os.path.exists("data/customer_data_collection.csv") and os.path.exists("data/product_recommendation_data.csv"):
    load_user_data()
    load_product_data()
else:
    st.warning("📂 Please upload both 'customer_data_collection.csv' and 'product_recommendation_data.csv' into the `data/` folder.")

user_id = st.text_input("Enter Customer ID (e.g., CUST123):")
product_id = st.text_input("Last Viewed Product ID (e.g., P11872):")

if st.button("Get Recommendations"):
    if not user_id or not product_id:
        st.warning("Please enter both Customer ID and Product ID.")
    else:
        log_interaction(user_id, product_id, action='click')
        recommendations = generate_recommendations(user_id)

        if recommendations:
            st.success(f"Top {len(recommendations)} Recommended Products for {user_id}:")
            for pid in recommendations:
                product = get_product_info(pid)
                if product:
                    st.markdown(f"""
                    **🛒 Product ID:** `{product[0]}`
                    - **Category:** {product[1]} | **Subcategory:** {product[2]} | **Brand:** {product[4]}
                    - **Price:** ₹{product[3]} | **Rating:** {product[6]}
                    ---
                    """)
        else:
            st.warning("No recommendations found for this user.")
