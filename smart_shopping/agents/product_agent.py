import sqlite3
from database.db_manager import get_connection

class ProductAgent:
    def __init__(self):
        self.conn = get_connection()

    def get_product_info(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()
        return product

if __name__ == '__main__':
    agent = ProductAgent()
    product = agent.get_product_info(101)
    print("Product Info:", product)
