from database.db_manager import get_connection

class ProductAgent:
    def get_product_info(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE Product_ID = ?", (product_id,))
        product = cursor.fetchone()
        conn.close()
        return product
