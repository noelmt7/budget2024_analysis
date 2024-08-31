from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
import time

# Load dataset
budget_data = pd.read_csv('merged_data.csv')

# Set API key directly
GROQ_API_KEY = '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'


# Streamlit UI
st.title("Budget 2024")
st.write("Enter a prompt to generate a response based on public opinions on the budget:")

# Input prompt
user_prompt = st.text_area("Prompt", "Provide details or questions about the public opinions on the budget:")

# Function to generate budget response
def generate_budget_response(prompt_message, data):
    # Truncate or summarize dataset to fit within context length limits
    data_summary = budget_data.head(5).to_string()[:1000]  # Limit summary to 1000 characters
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a knowledgeable analyst interpreting public opinions on the country's budget. Provide a detailed and insightful response based on the provided prompt and dataset."),
            ("user", f"Prompt: {prompt_message}\nPublic Opinion Dataset Summary: {data_summary}")
        ]
    )

    groqApi = ChatGroq(model="llama3-70b-8192", temperature=0.1, api_key=GROQ_API_KEY)
    outputparser = StrOutputParser()
    chainSec = prompt | groqApi | outputparser

    # Implement rate limiting logic
    max_tokens_per_minute = 5000
    start_time = time.time()
    token_usage = 0

    def rate_limit_check(tokens):
        nonlocal token_usage
        if token_usage + tokens > max_tokens_per_minute:
            elapsed_time = time.time() - start_time
            if elapsed_time < 60:  # Within the same minute
                wait_time = 60 - elapsed_time
                st.write(f"Rate limit exceeded. Waiting for {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            # Reset timer and token usage
            start_time = time.time()
            token_usage = 0

    # Generate budget response with rate limiting
    response = None
    try:
        rate_limit_check(1000)  # Estimate tokens for this request
        response = chainSec.invoke({'data': prompt_message})
        token_usage += len(response)  # Update with actual token usage
    except Exception as e:
        st.write(f"An error occurred: {e}")

    return response

if st.button("Generate Response"):
    if user_prompt.strip():  # Check if prompt is not empty
        budget_response = generate_budget_response(user_prompt, "")
        st.write("Generated Budget Response:")
        st.write(budget_response)
    else:
        st.write("Please enter a prompt to generate a response.")
