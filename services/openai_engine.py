from openai import AsyncOpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL, INSTRUCTIONS

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def ask_kimiko(message):
    response = await client.responses.create(
        model=OPENAI_MODEL,
        instructions=INSTRUCTIONS,
        input=message,
    )
    return response.output_text
