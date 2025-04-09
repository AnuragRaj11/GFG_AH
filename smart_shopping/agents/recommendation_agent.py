from database.db_manager import get_connection
from models.content_based_model import ContentBasedRecommender

class RecommendationAgent:
    def __init__(self):
        self.recommender = ContentBasedRecommender()

    def generate_recommendations(self, user_id=None, product_id=None):
        # Use provided product_id directly
        if product_id:
            return self.recommender.recommend(product_id)
        
        # Otherwise fallback to user's last viewed product from DB
        if user_id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT product_id FROM User_Interactions
                WHERE user_id = ?
                ORDER BY timestamp DESC LIMIT 1
            ''', (user_id,))
            last = cursor.fetchone()
            conn.close()
            if last:
                return self.recommender.recommend(last[0])

        # If neither worked
        return []
