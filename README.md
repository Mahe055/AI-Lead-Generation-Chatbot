Built an AI chatbot that converts user conversations into leads using intent detection and knowledge-based responses.# Social to Lead AI Agent

# Overview
This project is a simple AI-powered chatbot that converts user conversations into leads.

# Features
- Intent detection (greeting, pricing, buying intent)
- Knowledge-based responses using external files
- Lead capture system (name, email, platform)
- Fallback to LLM (Gemini API)

# Tech Stack
- Python
- LangChain
- Google Gemini API
- JSON (for structured knowledge)
- Text file (for document-based responses)

# How it Works
1. User enters a message
2. Intent is detected using rule-based + LLM fallback
3. Based on intent:
   - Greeting → Friendly response
   - Pricing → Reads from knowledge base
   - High Intent → Collects user details
4. Lead is captured and printed

# Setup

1. Install dependencies: