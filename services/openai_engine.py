from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL, INSTRUCTIONS

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model=OPENAI_MODEL,
    instructions=INSTRUCTIONS,
    input="Hello world",
)

print(response.output_text)