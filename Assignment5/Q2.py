# 2. ⁠Connect to Groq and Gemini AI using REST api. Send same prompt and compare results. Also compare the speed.

import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

PROMPT = "Explain Artificial Intelligence in simple words."

# -------------------- GROQ --------------------
def call_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }

    start = time.time()
    response = requests.post(url, headers=headers, json=data)
    end = time.time()

    reply = response.json()["choices"][0]["message"]["content"]
    return reply, end - start


# -------------------- GEMINI --------------------
def call_gemini(prompt):
    import requests, time, os

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GEMINI_API_KEY}"
    }

    data = {
        "prompt": {"text": prompt},
        "temperature": 0.7,
        "maxOutputTokens": 256
    }

    start = time.time()
    response = requests.post(url, headers=headers, json=data)
    end = time.time()

    response_json = response.json()
    print(response_json)
    # Updated parsing depending on the response structure
    if "candidates" in response_json:
        reply = response_json["candidates"][0]["content"]["parts"][0]["text"]
    elif "responses" in response_json:
        reply = response_json["responses"][0]["content"][0]["text"]
    elif "completion" in response_json:
        reply = response_json["completion"]["text"]
    else:
        reply = "No valid response found from Gemini."

    return reply, end - start


# -------------------- MAIN --------------------
print("\nPrompt:", PROMPT)

groq_reply, groq_time = call_groq(PROMPT)
print("\n--- GROQ RESPONSE ---")
print(groq_reply)
print(f"Time Taken: {groq_time:.3f} seconds")

gemini_reply, gemini_time = call_gemini(PROMPT)
print("\n--- GEMINI RESPONSE ---")
print(gemini_reply)
print(f"Time Taken: {gemini_time:.3f} seconds")

print("\n--- SPEED COMPARISON ---")
if groq_time < gemini_time:
    print("Groq is faster 🚀")
else:
    print("Gemini is faster 🚀")
