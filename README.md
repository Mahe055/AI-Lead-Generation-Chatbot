

# How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/your-username/Social-to-Lead-Agent.git

# 2. Go to project folder
cd Social-to-Lead-Agent

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key in .env file
GOOGLE_API_KEY=your_api_key_here

# 5. Run the chatbot
python main.py
```
# Architecture Explanation (~200 words)

This project implements a simple conversational agent that combines intent detection, structured knowledge retrieval, and lead capture.

LangChain is used for integrating the LLM (Google Gemini) and handling prompt-based intent classification fallback. Instead of using LangGraph or AutoGen, a lightweight procedural flow is used because the conversation logic is linear and does not require complex multi-agent coordination or graph-based state transitions.

State is managed using a Python dictionary (`user_data`) which stores user intent and lead information such as name, email, and platform. This allows the chatbot to maintain context across multiple turns, especially during the lead capture phase.

For knowledge retrieval, the system uses a local JSON file (`knowledge.json`) which contains structured data such as pricing plans and company policies. This approach ensures deterministic and accurate responses without relying entirely on the LLM. A simple keyword-based retrieval mechanism is used to simulate RAG behavior.

The architecture prioritizes simplicity, clarity, and reliability, making it suitable for small-scale automation tasks like lead generation and customer interaction.

# WhatsApp Deployment (Webhook Integration)

To integrate this chatbot with WhatsApp, we can use the WhatsApp Business API (via providers like Meta or Twilio).

The flow would work as follows:

1. A user sends a message on WhatsApp.
2. WhatsApp forwards this message to a backend server via a webhook (HTTP POST request).
3. The backend receives the message and passes it to the chatbot logic (`chatbot()` function).
4. The chatbot processes the input (intent detection, retrieval, or lead capture).
5. The generated response is sent back to WhatsApp using the API.
6. The user receives the reply instantly in the chat.

The webhook acts as the bridge between WhatsApp and the chatbot system. For production use, the chatbot logic would be wrapped inside a web framework like Flask or FastAPI, and deployed on a server to handle incoming requests in real-time.


