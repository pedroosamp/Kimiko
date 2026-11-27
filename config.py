from dotenv import load_dotenv

import os
from pathlib import Path

load_dotenv()

DATABASE_URL = os.getenv("database_url")

TOKEN = os.getenv("token")
PREFIX = os.getenv("prefix")
COMMANDS = []

OPENAI_API_KEY = os.getenv("openai_api_key")
OPENAI_MODEL = os.getenv("openai_model")
INSTRUCTIONS = Path("prompts/system.txt").read_text(encoding="utf-8")