import streamlit as st

st.title("Medical Chatbot")
st.write("This is a Medical bot which gives relavant answers for u r queries")
name = st.text_input("Enter Your Name ")
if name:
    st.write("Hi"+name)