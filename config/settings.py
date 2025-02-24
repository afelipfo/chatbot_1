#/config/settings.py

import os
from dotenv import load_dotenv

# ✅ Corrected LangChain Imports
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# ✅ Updated memory import
from langchain.memory import ConversationBufferMemory  

# ✅ Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DB_PATH = os.getenv("DB_PATH")

if not GOOGLE_API_KEY:
    raise ValueError("❌ Missing GOOGLE_API_KEY in .env file")
if not DB_PATH:
    raise ValueError("❌ Missing DB_PATH in .env file")

# ✅ Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# ✅ Use updated Chroma and OllamaEmbeddings
embedding_model = OllamaEmbeddings(model="mxbai-embed-large:latest")
vector_db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_model)

# ✅ Use `ConversationBufferMemory` to store chat history
classification_memory = ConversationBufferMemory(memory_key="classification_history")

shared_memory = ConversationBufferMemory(memory_key="history")

