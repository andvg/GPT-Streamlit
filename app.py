import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response["choices"][0]["text"]

def main():
    st.title("Text Generator")
    prompt = st.text_input("Prompt")
    if st.button("Generate"):
        st.write("Aieie!")