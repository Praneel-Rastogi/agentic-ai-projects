# main.py -- simple env-check for Summarizer Agent
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

def ok(env):
    v = os.getenv(env)
    return "✅ set" if v and len(v) > 10 else "⚠️ missing or short"

if __name__ == "__main__":
    print("Env check (summarizer-agent):")
    print("  OPENAI_API_KEY:", ok("OPENAI_API_KEY"))
    print("  SERPAPI_API_KEY:", ok("SERPAPI_API_KEY"))
    print("\nIf keys show ⚠️, paste them into projects/summarizer-agent/.env and re-run.")
