import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=60000),
)

models = [
    "gemini-3.5-flash-lite",
    "gemini-3.7-flash",
    "gemini-3.1-flash-lite",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.8-flash",
]

for name in models:
    try:
        r = client.models.generate_content(model=name, contents="Say hello in 3 words.")
        print(name, "-> OK:", r.text)
    except Exception as e:
        print(name, "-> FAILED:", str(e)[:150])