# ================================
# Dolor3v - My Personal Coding AI
# ================================

import requests
from pathlib import Path

env = {}
if Path(".env").exists():
    for line in open(".env"):
        if "=" in line:
            k, v = line.strip().split("=", 1)
            env[k] = v

GROQ_API_KEY = env.get("GROQ_API_KEY", "")
OPENROUTER_API_KEY = env.get("OPENROUTER_API_KEY", "")

def ask_groq(prompt):
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are Dolor3v, an expert software engineer. Write clean production-ready code."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    data = r.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    return None

def ask_openrouter(prompt):
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/dolordprince",
            "X-Title": "Dolor3v"
        },
        json={
            "model": "google/gemma-4-31b-it:free",
            "messages": [
                {"role": "system", "content": "You are Dolor3v, an expert software engineer. Write clean production-ready code."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    data = r.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    return None

def ask(prompt):
    print("\nDolor3v thinking...\n")
    result = ask_groq(prompt)
    if result:
        print("[Powered by Groq]\n")
        return result
    print("Groq unavailable, switching to backup...\n")
    result = ask_openrouter(prompt)
    if result:
        print("[Powered by OpenRouter]\n")
        return result
    return "All engines unavailable. Try again later."

print("=" * 40)
print("  Dolor3v - Your Personal Coding AI")
print("=" * 40)

while True:
    q = input("\nDolor3v> ")
    if q.lower() in ["quit", "exit"]:
        print("Dolor3v shutting down. Goodbye!")
        break
    print(ask(q))
