import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

if not API_KEY:
    raise ValueError("API_KEY is missing. Check your .env file.")

if not BASE_URL:
    raise ValueError("BASE_URL is missing. Check your .env file.")
