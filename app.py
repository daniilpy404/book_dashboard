import streamlit as st
from db import get_data

st.set_page_config(page_title="Book Dashboard", layout="wide")

st.title("📚 Book Dashboard")

df = get_data()

genres = df["genre"].unique()
selected_genre = st.selectbox("Выбери жанр", ["Все"] + list(genres))

if selected_genre != "Все":
    df = df[df["genre"] == selected_genre]

st.write(f"Найдено книг: {len(df)}")

for _, row in df.iterrows():
    st.markdown(f"""
    ### {row['title']}
    - Жанр: {row['genre']}
    - Цена: {row['price']}
    - [Ссылка]({row['link']})
    """)