import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=120000),
)

MODEL = "gemini-3.5-flash"


def ask(prompt, temperature=1.0, system=None):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    system_instruction=system,
                ),
            )
            return response.text
        except Exception as e:
            print("Error:", e)
            print("Waiting 20 seconds...")
            time.sleep(20)
    return "Failed after 3 tries"


prompts = [
    "What is 37 times 48?",
    "Who won the 2050 football World Cup?",
    "Summarize the 2019 research paper 'Quantum Banana Networks for Credit Scoring' by Dr. R. Menon.",
    "What is the capital of Australia?",
    "Write a haiku about monsoon rain.",
    "Explain overfitting in one sentence.",
    "Give me three prompt ideas for testing a chatbot, as a numbered list.",
    "Extract the name and city as JSON: 'Aditya lives in Pathri and likes data science.'",
    "What did I eat for breakfast today?",
    "Say 'I don't know' if you are not sure: what is the population of the village of Pathri, Maharashtra, exactly?",
]

for i, p in enumerate(prompts, start=1):
    print(i, "PROMPT:", p)
    print("ANSWER:", ask(p, temperature=0.0))
    print()
    time.sleep(2)