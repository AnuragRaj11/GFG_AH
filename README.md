 # 🛍️ Smart Shopping AI Recommender System

An AI-powered product recommendation system built for the Gen AI Hackathon, solving **Problem Statement 2: Smart Shopping**. This project leverages multi-agent architecture and machine learning to deliver hyper-personalized recommendations based on customer interactions.

---

## 🚀 Features

- ✅ Multi-Agent Architecture
- ✅ Content-Based Filtering using TF-IDF & Cosine Similarity
- ✅ SQLite for persistent memory (Users, Products, Interactions)
- ✅ Streamlit Web Interface for live demo

---

## 📁 Project Structure

```bash
smart_shopping/
├── app.py                      # Main script for CLI testing
├── streamlit_app.py           # Web app using Streamlit (to be created)
├── requirements.txt
│
├── agents/
│   ├── customer_agent.py      # Logs customer interactions
│   ├── product_agent.py       # Retrieves product info
│   └── recommendation_agent.py # Generates personalized suggestions
│
├── database/
│   └── db_manager.py          # SQLite database management & table creation
│
├── models/
│   └── content_based_model.py # ML model using TF-IDF & Cosine Similarity
│
├── utils/
│   └── data_loader.py         # Loads CSV data into SQLite tables
│
├── data/
│   ├── customer_data_collection.csv
│   └── product_recommendation_data.csv
└── smart_shopping.db          # SQLite database file
```

> **Note:** If `streamlit_app.py` is not yet created, run `touch smart_shopping/streamlit_app.py` and copy the Streamlit UI code into it.

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourname/smart-shopping-ai
cd smart-shopping-ai

# (Optional) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 How to Run

### 🖥️ CLI Mode
```bash
python app.py
```

### 🌐 Web App (Streamlit)
First, create `streamlit_app.py` with the UI logic.

Then run:
```bash
streamlit run streamlit_app.py
```

Visit: http://localhost:8501

---

## 📊 Dataset Columns

### Customers
- `Customer_ID`
- `Gender`, `Age`, `Location`, `Marital_Status`
- `Purchase_History`

### Products
- `Product_ID`
- `Category`, `Subcategory`, `Brand`, `Price`
- `Season`, `Geographical_Location`, `description (synthetic)`

---

## 📌 How It Works

1. Logs customer interactions (e.g., viewing a product).
2. Extracts content-based features.
3. Uses TF-IDF to vectorize descriptions.
4. Computes similarity between products.
5. Returns top-N most similar items.
6. Displays results on terminal or Streamlit UI.

---

## 🧠 Tech Stack
- Python 3.x
- pandas, scikit-learn, sqlite3
- Streamlit (for UI)

---

## 🙌 Contributing
Pull requests and ideas are welcome!

---

## 🏆 Built for
**Gen AI Hackathon**

> Problem Statement 2: Smart Shopping – Data & AI for Personalized E-Commerce

---

## 📜 License
MIT License

