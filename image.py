from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

client = OpenAI()

response = client.images.generate(
model="dall-e-2",
prompt="A beautiful image of a cat",
size="1024x1024",
quality="standard",
n=1,
)
