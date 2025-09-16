# Summarizer Agent 📝

An autonomous agent that can **search the web** and **summarize results** into clear, concise insights.  
Built with **LangChain** + **OpenAI** + (optionally) **SerpAPI**.

---

## 🚀 Features
- Accepts a natural language query.
- Uses a search tool (SerpAPI / DuckDuckGo) to retrieve relevant information.
- Summarizes results using LLM (OpenAI GPT model).
- Outputs clean bullet-pointed answers.

---

## 📂 Project Structure
summarizer-agent/
│── main.py # Entry point
│── requirements.txt # Dependencies
│── .env.example # API key placeholders
│── README.md # This file


---

## ⚙️ Setup & Installation

1. **Clone repo**
   ```bash
   git clone https://github.com/Praneel-Rastogi/agentic-ai-projects.git
   cd agentic-ai-projects/projects/summarizer-agent

2. **Create virtual environment**

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. **Install dependencies**

pip install -r requirements.txt

4. **Setup environment variables**
Copy .env.example → rename to .env → fill in your API keys.

## ▶️ Running the Agent
python main.py

### Example:
Enter your query: What are the key highlights of Apple’s latest iPhone release?

### Output:
🔎 Searching...
📑 Summarizing...
✅ Key Insights:
- Feature 1
- Feature 2
- ...

## 🛠️ Tech Stack

LangChain – orchestration

OpenAI API – summarization

SerpAPI / DuckDuckGo – search

## 📌 Next Steps

Add memory for multi-turn queries

Experiment with different LLMs

Improve prompt engineering

Export results to markdown/pdf