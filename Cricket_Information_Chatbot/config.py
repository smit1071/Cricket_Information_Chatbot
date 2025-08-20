import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# Loading Groq API Key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Chat model
def load_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="gemma2-9b-it",  
    )
