from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent
from utils.data_loader import load_user_data, load_product_data
from database.db_manager import create_tables

def main():
    print("⏳ Setting up...")
    create_tables()
    load_user_data()
    load_product_data()

    customer_agent = CustomerAgent()
    product_agent = ProductAgent()
    rec_agent = RecommendationAgent()

    user_id = 'CUST123'  # Replace with real Customer_ID from dataset
    product_id = 'P11872'  # Replace with Product_ID
    action = 'click'

    customer_agent.log_interaction(user_id, product_id, action)

    print(f"🔍 Recommendations for {user_id}:")
    recommendations = rec_agent.generate_recommendations(user_id)
    for pid in recommendations:
        print(product_agent.get_product_info(pid))

if __name__ == '__main__':
    main()
