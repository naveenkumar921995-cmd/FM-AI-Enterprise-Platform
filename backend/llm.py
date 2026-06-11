from langchain_groq import ChatGroq
from backend.config import GROQ_API_KEY

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Configure it in environment variables or Streamlit secrets."
    )

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)
