# 📊 Book Dashboard

An interactive Streamlit dashboard for exploring book data collected via web scraping, featuring PostgreSQL integration, genre-based filtering, and a clean user interface for data visualization.

---

## 🚀 Features

- 📚 Display book dataset (title, genre, price, link)
- 🎯 Filter books by genre
- 🔎 Easy data exploration interface
- ⚡ Fast and lightweight UI built with Streamlit
- 🛢 PostgreSQL integration

---

## 🏗 Project Structure


book_dashboard/
│
├── app.py # Streamlit app
├── db.py # Database connection & queries
├── config.py # Configuration (DB credentials)
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone the repository


git clone https://github.com/yourusername/book_dashboard.git
cd book_dashboard


### 2. Install dependencies


pip install -r requirements.txt


---

## 🛢 Database Setup

Make sure PostgreSQL is installed and running.

Create database:

```sql
CREATE DATABASE books_db;

Update credentials in config.py:

DB_CONFIG = {
    "dbname": "books_db",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}
▶️ Usage

Run the app:

streamlit run app.py

Open in browser:

http://localhost:8501
🧠 Tech Stack
Python
Streamlit
PostgreSQL
Pandas
psycopg2
🔮 Future Improvements
🔍 Search by title
📊 Price analytics & charts
🌐 Deployment (Streamlit Cloud / Docker)
🔐 Environment variables (.env)
❤️ Favorites / user interaction
⚠️ Disclaimer

This project is built for educational purposes.
Ensure compliance with website terms before scraping data.

👨‍💻 Author

Developed as a full-cycle data project: from web scraping and data storage to interactive visualization.