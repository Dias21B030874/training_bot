# Configuration settings for the application

import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    DATABASE_URL = "sqlite:///database.db"  # SQLite database URL
    # Add other configuration settings as needed