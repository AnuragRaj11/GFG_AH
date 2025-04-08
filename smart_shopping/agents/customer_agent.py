from database.db_manager import get_connection
from datetime import datetime

class CustomerAgent:
    def log_interaction(self, user_id, product_id, action):
        conn = get_connection()
        cursor = conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute('''
            INSERT INTO User_Interactions (user_id, product_id, action, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (user_id, product_id, action, timestamp))
        conn.commit()
        conn.close()
