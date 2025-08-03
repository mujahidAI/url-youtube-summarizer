🦜 URL & YouTube Summarizer with LangChain + Groq

A sleek and powerful Streamlit web app that summarizes content from YouTube videos and web pages using LangChain, Groq LLMs (llama3-8b-8192), and intelligent prompt engineering. Whether it’s a lecture, article, or interview — get the core insights in under 300 words.
✨ Features

    🔗 Summarize content from any valid URL (web article or YouTube).

    📽️ Automatic transcript parsing for YouTube videos.

    🧠 Uses Groq-hosted LLM models via LangChain.

    📄 Extracts main points, insights, and takeaways.

    🎯 Clean and focused summary (max 300 words).

    🔐 API key is secured via Streamlit input.

🛠️ Tech Stack

    Streamlit – UI

    LangChain – Orchestration

    Groq – Fast inference for LLMs (LLaMA 3 / Gemma)

    YoutubeLoader – Transcripts from YouTube

    UnstructuredURLLoader – Web scraping

    RecursiveCharacterTextSplitter – Document chunking

    validators – URL validation

🧪 How It Works

    User submits a valid YouTube or webpage URL.

    Content is loaded using the appropriate loader.

    Text is split into digestible chunks.

    LLM generates summaries using a map-reduce summarization chain.

    Final summary is displayed on screen.

🧰 Setup Instructions

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run e4ef2907-a1a5-42dc-87f0-95eb6d51fa1b.py

🔑 Environment Variables

Create a .env or input in-app:

    GROQ_API_KEY: Your Groq API key (entered in sidebar).

📌 Notes

    Only URLs from YouTube or web articles are supported.

    Summarization uses llama3-8b-8192 by default (you can modify to use other Groq-supported models).

    Streamlit UI is kept minimal for focus and speed.
