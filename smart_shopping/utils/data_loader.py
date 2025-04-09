import pandas as pd
import os
import sqlite3
import logging
import streamlit as st
from typing import Optional
from database.db_manager import get_connection, create_tables

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_user_data(path: str = 'data/customer_data_collection.csv') -> Optional[pd.DataFrame]:
    """
    Load user data from CSV and insert into SQLite database.
    
    Args:
        path (str): Path to the CSV file. Defaults to 'data/customer_data_collection.csv'.
    
    Returns:
        pd.DataFrame: Loaded DataFrame if successful, None otherwise.
    """
    try:
        if not os.path.exists(path):
            st.error(f"❌ Missing file: {path}")
            logger.error(f"User data file not found: {path}")
            return None

        df = pd.read_csv(path)
        conn = get_connection()
        df.to_sql('Users', conn, if_exists='replace', index=False)
        conn.commit()
        logger.info("✅ Successfully loaded user data into database.")
        return df

    except Exception as e:
        st.error(f"❌ Failed to load user data: {e}")
        logger.error(f"Error loading user data: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()

@st.cache_data  # Cache to avoid reloading in Streamlit
def load_product_data(path: str = 'data/product_recommendation_data.csv') -> Optional[pd.DataFrame]:
    """
    Load product data from CSV and insert into SQLite database.
    
    Args:
        path (str): Path to the CSV file. Defaults to 'data/product_recommendation_data.csv'.
    
    Returns:
        pd.DataFrame: Loaded DataFrame if successful, None otherwise.
    """
    try:
        if not os.path.exists(path):
            st.error(f"❌ Missing file: {path}")
            logger.error(f"Product data file not found: {path}")
            return None

        df = pd.read_csv(path)
        conn = get_connection()
        df.to_sql('Products', conn, if_exists='replace', index=False)
        conn.commit()
        logger.info("✅ Successfully loaded product data into database.")
        return df

    except Exception as e:
        st.error(f"❌ Failed to load product data: {e}")
        logger.error(f"Error loading product data: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()