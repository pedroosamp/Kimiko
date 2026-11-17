from dotenv import load_dotenv

import os
from pathlib import Path

load_dotenv()

TOKEN = os.getenv("token")
PREFIX = os.getenv("prefix")
COMMANDS = {}

OPENAI_API_KEY = os.getenv("openai_api_key")
OPENAI_MODEL = "gpt-5-mini"
INSTRUCTIONS = Path("prompts/system.txt").read_text(encoding="utf-8")