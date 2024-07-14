from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    
    SQLITE_DB_URL = os.getenv('SQLITE_DB_URL')