import streamlit as st
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from utils.data_loader import load_user_data, load_product_data
from database.db_manager import create_tables

# Setup DB and load data
create_tables()
load_user_data()
load_product_data()

st.set_page_config(page_title="Smart Shopping Recommender", layout="centered")
st.title("🛍️ Smart Shopping AI Recommender")

user_id = st.text_input("Enter Customer ID (e.g., CUST123):")
product_id = st.text_input("Last Viewed Product ID (e.g., P11872):")

if st.button("Get Recommendations"):
    if not user_id or not product_id:
        st.warning("Please enter both Customer ID and Product ID.")
    else:
        customer_agent = CustomerAgent()
        product_agent = ProductAgent()
        rec_agent = RecommendationAgent()

        customer_agent.log_interaction(user_id, product_id, action='click')

        recommendations = rec_agent.generate_recommendations(user_id)

        if recommendations:
            st.success(f"Top {len(recommendations)} Recommended Products for {user_id}:")
            for pid in recommendations:
                product = product_agent.get_product_info(pid)
                if product:
                    st.markdown(f"""
                    **🛒 Product ID:** `{product[0]}`
                    - **Category:** {product[1]} | **Subcategory:** {product[2]} | **Brand:** {product[4]}
                    - **Price:** ₹{product[3]} | **Rating:** {product[5]}
                    ---
                    """)
        else:
            st.warning("No recommendations found for this user.")
