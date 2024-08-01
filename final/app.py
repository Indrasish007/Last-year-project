import streamlit as st
if st.button("home"):
    st.switch_page("app.py")
if st.button("stock"):
    st.switch_page("pages/stock.py")
if st.button("whatsapp"):
    st.switch_page("pages/whatsapp.py")