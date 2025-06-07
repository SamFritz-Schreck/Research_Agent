import streamlit as st

from langchain_ollama import ChatOllama

chat_model = ChatOllama(model="llama3.1:8b")

print(chat_model.invoke("Who was the first man on the moon?"))