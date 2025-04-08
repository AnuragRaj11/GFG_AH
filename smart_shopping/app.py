from agents.customer_agent import CustomerAgent
from agents.recommendation_agent import RecommendationAgent
from agents.product_agent import ProductAgent

def main():
    # Initialize agents
    customer_agent = CustomerAgent()
    rec_agent = RecommendationAgent()
    product_agent = ProductAgent()

    # Simulate a customer interaction:
    # Assume user 1 clicks on product 101
    customer_agent.log_interaction(user_id=1, product_id=101, action='click')

    # Generate recommendations based on user history
    recommendations = rec_agent.generate_recommendations(user_id=1)
    print("Final Recommendations for User 1:", recommendations)

    # Optionally, fetch and display product details for one recommended product:
    if recommendations:
        product_details = product_agent.get_product_info(recommendations[0])
        print("Details for recommended product:", product_details)

if __name__ == '__main__':
    main()
