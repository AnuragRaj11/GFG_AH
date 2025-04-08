import sqlite3
from datetime import datetime
from utils.embedding import get_product_embedding, cosine_similarity
from database.db_manager import get_connection

class RecommendationAgent:
    def __init__(self):
        self.conn = get_connection()

    def fetch_user_history(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT product_id FROM User_Interactions WHERE user_id = ?", (user_id,))
        results = cursor.fetchall()
        return [row[0] for row in results]

    def fetch_product_description(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT description FROM Products WHERE product_id = ?", (product_id,))
        result = cursor.fetchone()
        return result[0] if result else ""

    def find_similar_products(self, target_embedding):
     cursor = self.conn.cursor()
     cursor.execute("SELECT product_id, description FROM Products")
     candidates = cursor.fetchall()
     similar_products = []
     for product_id, description in candidates:
        embedding = get_product_embedding(description)
        similarity = cosine_similarity(target_embedding, embedding)
        print(f"Product {product_id} similarity: {similarity}")  # Debug print
        if similarity > 0.95:
            similar_products.append(product_id)
     return similar_products

    def generate_recommendations(self, user_id):
        user_history = self.fetch_user_history(user_id)
        recommendations = set()
        for product_id in user_history:
            description = self.fetch_product_description(product_id)
            embedding = get_product_embedding(description)
            similar = self.find_similar_products(embedding)
            recommendations.update(similar)
        recommendations = list(recommendations)
        # Log recommendations in the database
        self.log_recommendations(user_id, recommendations)
        return recommendations

    def log_recommendations(self, user_id, recommendations):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Recommendations (user_id, recommended_products, timestamp)
            VALUES (?, ?, ?)
        """, (user_id, ','.join(map(str, recommendations)), datetime.now().isoformat()))
        self.conn.commit()

if __name__ == '__main__':
    rec_agent = RecommendationAgent()
    recs = rec_agent.generate_recommendations(user_id=1)
    print("Recommended products for user 1:", recs)
