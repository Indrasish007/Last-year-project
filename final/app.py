import streamlit as st
if st.button("home"):
    st.switch_page("app.py")
if st.button("Stock price prediction"):
    st.switch_page("pages/stock.py")
if st.button("Whatsapp Chat Analyzer"):
    st.switch_page("pages/whatsapp.py")
if st.button("Car price"):
    st.switch_page("pages/car.py")

