
#  AI Lead Generation Chatbot

This project is a simple chatbot built using Python and LangChain.
It can answer user queries about pricing and collect basic details from users who show interest in buying a plan.


#  Features

* Basic conversational chatbot (runs in terminal)
* Intent detection using rules + LLM fallback
* Answers pricing-related questions
* Captures user details (name, email, platform)
* Uses `.env` for API key security


#  Tech Stack

* Python
* LangChain
* Google Gemini API
* dotenv

#  How it works

* The chatbot first tries to detect intent using simple keyword rules
* If that fails, it uses the LLM
* Based on intent:

  * greeting → responds normally
  * pricing → shows plan details
  * buying intent → collects user info


#  Example

You: hello
Bot: Hi! You can ask about pricing or plans 😊

You: pricing
Bot: Basic Plan: $29/month...
Bot: Pro Plan: $79/month...

You: I want to buy
Bot: What's your name?


#  Author

Mahesh


