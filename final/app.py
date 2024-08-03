import streamlit as st

col1,col2,col3,col4=st.columns([1,1,1,1])
with col1:
    if st.button("Home Page"):
        st.switch_page("app.py")
with col2:
    if st.button("Stock Price Prediction"):
        st.switch_page("pages/stock.py")
with col3:
    if st.button("Whatsapp Chat Analyzer"):
        st.switch_page("pages/whatsapp.py")
with col4:
    if st.button("Car Price Prediction"):
        st.switch_page("pages/car.py")

