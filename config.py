from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("token")
PREFIX = os.getenv("prefix")
COMMANDS = {}