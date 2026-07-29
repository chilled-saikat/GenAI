from google import genai
from config import API
client=genai.Client(api_key=API)
import streamlit as st

st.set_page_config(
    page_title="Gemini Powered Chatbot",
    page_icon=":robot:",
    layout="wide"
)

st.header("Gemini Powered Chatbot")
st.write("This is a AI Powered Chatbot for Intraction")
st.subheader("Input Your Question")

input= st.text_input("You Question: ")

if st.button("Enter Your Question"):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=input
    )
    st.subheader("Bot Answer:")
    st.success(response.text)