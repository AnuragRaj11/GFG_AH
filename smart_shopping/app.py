import os
import streamlit as st
from database.db_manager import create_tables
from utils.data_loader import load_user_data, load_product_data
from agents.recommendation_agent import RecommendationAgent
from agents.product_agent import ProductAgent

# Debug: Check working directory and list files in data folder
st.write("Current working directory:", os.getcwd())
try:
    st.write("Files in data folder:", os.listdir("data"))
except Exception as e:
    st.error("Error accessing data folder: " + str(e))

# Streamlit UI
st.set_page_config(page_title="Smart Shopping Recommender", layout="centered")
st.title("🛍️ Smart Shopping AI Recommender")

# Initialize database and load data
create_tables()

# Use constructed absolute paths (if needed):
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
user_data_path = os.path.join(BASE_DIR, "data", "customer_data_collection.csv")
product_data_path = os.path.join(BASE_DIR, "data", "product_recommendation_data.csv")

if os.path.exists(user_data_path) and os.path.exists(product_data_path):
    load_user_data(user_data_path)
    load_product_data(product_data_path)
else:
    st.warning("📂 Please upload both 'customer_data_collection.csv' and 'product_recommendation_data.csv' into the `data/` folder.")

# Initialize agents
recommendation_agent = RecommendationAgent()
product_agent = ProductAgent()

# Input Section
user_id = st.text_input("Enter Customer ID (e.g., CUST123):")
product_id = st.text_input("Last Viewed Product ID (e.g., P11872):")

if st.button("Get Recommendations"):
    if not user_id or not product_id:
        st.warning("Please enter both Customer ID and Product ID.")
    else:
        recommendations = recommendation_agent.generate_recommendations(user_id, product_id)
        if recommendations:
            st.success(f"Top {len(recommendations)} Recommended Products for {user_id}:")
            for pid in recommendations:
                product = product_agent.get_product_info(pid)
                if product:
                    st.markdown(f"""
                    **🛒 Product ID:** `{product[0]}`
                    - **Category:** {product[1]} | **Subcategory:** {product[2]} | **Brand:** {product[4]}
                    - **Price:** ₹{product[3]} | **Rating:** {product[6]}
                    ---
                    """)
        else:
            st.warning("No recommendations found. This could be because:")
            st.write("- The product has no valid description")
            st.write("- There aren't enough similar products in the database")
            st.write("- This is a new user with no interaction history")
