from database.db_manager import get_connection
from models.content_based_model import ContentBasedRecommender

class RecommendationAgent:
    def __init__(self):
        self.recommender = ContentBasedRecommender()

    def generate_recommendations(self, user_id):
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
        else:
            return []
