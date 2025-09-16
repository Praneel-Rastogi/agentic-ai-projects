# summarizer-agent/src/main.py
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env in the same folder when running from this folder

def ok(env):
    v = os.getenv(env)
    return "✅ set" if v and len(v) > 10 else "⚠️ missing or short"

if __name__ == "__main__":
    print("Env check:")
    print("  OPENAI_API_KEY:", ok("OPENAI_API_KEY"))
    print("  SERPAPI_API_KEY:", ok("SERPAPI_API_KEY"))
    print("\nIf keys show ⚠️, paste them into summarizer-agent/.env and re-run.")
