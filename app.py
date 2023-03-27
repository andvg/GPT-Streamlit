import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def main():
    st.title("Text Generator")
    prompt = st.text_input("Prompt")
    models = [	"gpt-4", "gpt-4-0314", "gpt-4-32k", "gpt-4-32k-0314", "gpt-3.5-turbo", "gpt-3.5-turbo-0301"]
    model = st.selectbox("Model", models)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
        ]
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=1,0, step=0.1, help="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.")
    top_p = st.slider("Top P", min_value=0.1, max_value=1.0, value=1,0, step=0.1, help="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.")
    max_tokens = st.slider("Max tokens", min_value=10, max_value=1000, value=1000, step=10, help="The maximum number of tokens to generate in the chat completion.")
    if st.button("Generate"):
        st.write(messages)

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

if __name__ == "__main__":
    main()