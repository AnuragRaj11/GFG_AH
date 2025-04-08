import sqlite3
from datetime import datetime
from database.db_manager import get_connection

class CustomerAgent:
    def __init__(self):
        self.conn = get_connection()

    def log_interaction(self, user_id, product_id, action):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO User_Interactions (user_id, product_id, timestamp, action)
            VALUES (?, ?, ?, ?)
        """, (user_id, product_id, datetime.now().isoformat(), action))
        self.conn.commit()
        print(f"Logged interaction for user {user_id} on product {product_id} with action '{action}'.")

    def update_user_profile(self, user_id, new_preferences):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE Users SET preferences = ?
            WHERE user_id = ?
        """, (new_preferences, user_id))
        self.conn.commit()
        print(f"Updated preferences for user {user_id}.")

if __name__ == '__main__':
    agent = CustomerAgent()
    # Example usage: log a click interaction
    agent.log_interaction(user_id=1, product_id=101, action='click')
