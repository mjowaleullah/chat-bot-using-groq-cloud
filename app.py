import streamlit as st
from api_calling import *




st.title("Hey! I am  Your Chatbot :streamlit:")
st.markdown("Please Share Your any kind of story, History, Emotion etc")
st.markdown( "Developed By :copyright:[mjowaleullah](https://facebook.com/md.owaleullah) ")
st. divider()

with st.spinner("Processing Your Message..."):
    content = st.chat_input("Write your Message here....")

    if content:
        process = responser(content)
        st.markdown(process)
