# smart_shopping/app.py
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from utils.data_loader import load_user_data, load_product_data
from database.db_manager import create_tables

def main():
    print("\n[Setup] Initializing database and loading data...")
    create_tables()
    load_user_data()
    load_product_data()

    customer_agent = CustomerAgent()
    product_agent = ProductAgent()
    rec_agent = RecommendationAgent()

    user_id = 'CUST123'  # Example Customer_ID from your dataset
    product_id = 'P11872'  # Example Product_ID
    action = 'click'

    customer_agent.log_interaction(user_id, product_id, action)

    print(f"\n[Recommend] Top products for user {user_id}:")
    recommendations = rec_agent.generate_recommendations(user_id)
    for pid in recommendations:
        product = product_agent.get_product_info(pid)
        if product:
            print(f"Product ID: {product[0]}")
            print(f"Category: {product[1]} | Subcategory: {product[2]} | Brand: {product[4]}")
            print(f"Price: ₹{product[3]} | Rating: {product[5]}")
            print("---")

if __name__ == '__main__':
    main()