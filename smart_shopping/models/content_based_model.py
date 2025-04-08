import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database.db_manager import get_connection

class ContentBasedRecommender:
    def __init__(self):
        self.df = self._load_data()
        self.sim_matrix = self._build_similarity_matrix()

    def _load_data(self):
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM Products", conn)

        # Create synthetic description using available columns
        df['description'] = (
            df['Category'].fillna('') + ' ' +
            df['Subcategory'].fillna('') + ' ' +
            df['Brand'].fillna('') + ' ' +
            df['Season'].fillna('') + ' ' +
            df['Geographical_Location'].fillna('')
        )

        df['combined'] = df['description']
        conn.close()
        return df

    def _build_similarity_matrix(self):
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['combined'])
        return cosine_similarity(tfidf_matrix)

    def recommend(self, product_id, top_n=5):
        if product_id not in self.df['Product_ID'].values:
            return []

        idx = self.df.index[self.df['Product_ID'] == product_id][0]
        sim_scores = list(enumerate(self.sim_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        recommended_ids = [self.df.iloc[i[0]]['Product_ID'] for i in sim_scores]
        return recommended_ids
