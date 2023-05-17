import streamlit as st
import pandas as pd


st.set_page_config(page_title="Mahmoud Taha | Portfolio", page_icon="assets/images/web_icon.ico",
                   layout="centered", initial_sidebar_state="auto", menu_items=None)
col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("assets/images/photo.jpg")

with col2:
    st.title('Mahmoud Taha')
    title_content = """Hi, My name is Mahmoud Taha! I am an engineer,
                 python developer and full stack web developer."""
    st.info(title_content, icon="🚀")

contact_content = """Blow you can find some of the apps that I have built in Python. Feel free to contact me!"""
st.info(contact_content, icon="💡")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("assets/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("assets/images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("assets/images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")