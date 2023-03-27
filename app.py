import streamlit as st
import openai

openai.api_key = OPENAI_API_KEY

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

st.json(completion.to_dict())