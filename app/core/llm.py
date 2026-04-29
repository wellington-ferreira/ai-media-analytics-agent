from langchain.chat_models import init_chat_model
import os

llm = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider="groq",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

