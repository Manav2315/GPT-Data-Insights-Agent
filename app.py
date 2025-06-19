import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent

# Load API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("GPT Data Insights Agent")
st.markdown("Ask questions about your uploaded CSV file in plain English.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file and openai_api_key:
    df = pd.read_csv(uploaded_file)
    df.to_csv("temp.csv", index=False)
    st.write("Data Preview:", df.head())

    query = st.text_input("Enter your question")
    if query:
        llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
        agent = create_csv_agent(llm, "temp.csv", verbose=True)
        response = agent.run(query)
        st.success(response)
else:
    st.warning("Please upload a CSV file and make sure your OpenAI API key is set in the .env file.")