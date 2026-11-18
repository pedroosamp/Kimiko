from openai import AsyncOpenAI, AuthenticationError

from config import OPENAI_API_KEY, OPENAI_MODEL, INSTRUCTIONS

class KimikoOpenAI:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    async def verify_credentials(self):
        if not OPENAI_API_KEY:
            return False
        if not OPENAI_MODEL:
            raise ValueError("OPENAI_MODEL not set on .env")

        try:
            response = await AsyncOpenAI(api_key=OPENAI_API_KEY).responses.create(model=OPENAI_MODEL, input="Say: Working!")
            return True
        except AuthenticationError:
            print("AI responses are not available: Incorrect OPENAI_API_KEY provided.")
            return False

    async def ask_kimiko(self, message):
        response = await self.client.responses.create(
            model=OPENAI_MODEL,
            instructions=INSTRUCTIONS,
            input=message,
        )
        return response.output_text
