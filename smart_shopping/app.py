import os
import streamlit as st
from database.db_manager import create_tables
from data_loader import load_user_data, load_product_data
from recommendation_agent import RecommendationAgent
from product_agent import ProductAgent

# Streamlit UI
st.set_page_config(page_title="Smart Shopping Recommender", layout="centered")
st.title("🛍️ Smart Shopping AI Recommender")

# Initialize database and load data
create_tables()
if os.path.exists("data/customer_data_collection.csv") and os.path.exists("data/product_recommendation_data.csv"):
    load_user_data()
    load_product_data()
else:
    st.warning("📂 Please upload both 'customer_data_collection.csv' and 'product_recommendation_data.csv' into the `data/` folder.")

# Initialize agents
recommendation_agent = RecommendationAgent()
product_agent = ProductAgent()

user_id = st.text_input("Enter Customer ID (e.g., CUST123):")
product_id = st.text_input("Last Viewed Product ID (e.g., P11872):")

if st.button("Get Recommendations"):
    if not user_id or not product_id:
        st.warning("Please enter both Customer ID and Product ID.")
    else:
        recommendations = recommendation_agent.generate_recommendations(user_id)

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