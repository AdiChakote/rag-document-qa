import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

questions = [
    "Explain what an LLM is in 2 sentences.",
    "Explain photosynthesis in one sentence.",
    "Explain photosynthesis like I'm 5."
]

for q in questions:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model = "gemini-3.8-flash",
                contents = q
            )
                    
            print("Q", q)
            print("A", response.text)
            print()
            break
        except Exception as e:
            print("Busy or error, waiting 20 seconds...")
            time.sleep(20)