from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    
    
    SQLITE_DB_URL = os.getenv('SQLITE_DB_URL')
    
    OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL')
    
    
    ## API KEYS
    LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2')
    LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
    
    
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')