from database.db_manager import get_connection
from models.content_based_model import ContentBasedRecommender

class RecommendationAgent:
    def __init__(self):
        self.recommender = ContentBasedRecommender()

    def generate_recommendations(self, user_id=None, product_id=None):
        # Use provided product_id directly (after stripping whitespace)
        if product_id and product_id.strip():
            return self.recommender.recommend(product_id.strip())
        
        # Otherwise, fallback to the user's last viewed product from the database
        if user_id:
            try:
                with get_connection() as conn:  # Requires get_connection() to return a context manager
                    cursor = conn.cursor()
                    cursor.execute('''
                        SELECT product_id FROM User_Interactions
                        WHERE user_id = ?
                        ORDER BY timestamp DESC LIMIT 1
                    ''', (user_id,))
                    last = cursor.fetchone()
            except Exception as e:
                # Optionally log the error here
                last = None
            
            if last:
                return self.recommender.recommend(last[0])

        # If neither worked, return an empty list
        return []
