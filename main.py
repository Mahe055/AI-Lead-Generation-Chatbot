from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os
import json
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("GOOGLE_API_KEY"))

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.3
)
# Load knowledge JSON
with open("knowledge.json", "r") as f:
    knowledge = json.load(f)

# Lead capture
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

# Memory
user_data = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

def detect_intent(user_input):
    user_input_lower = user_input.strip().lower()

    if any(word in user_input_lower for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in user_input_lower for word in ["buy", "want", "purchase", "subscribe"]):
        return "high_intent"

    if any(word in user_input_lower for word in ["price", "pricing", "cost", "plan"]):
        return "pricing"

    if any(word in user_input_lower for word in ["refund"]):
        return "refund"

    if any(word in user_input_lower for word in ["support"]):
        return "support"
    
    if any(word in user_input_lower for word in ["ok", "okay", "fine", "cool", "alright", "sounds good", "great"
]):
        return "ack"
    
    return "unknown"


def chatbot():
    print("Bot: Hello! How can I help you?")

    while True:
        user = input("You: ")

        intent = detect_intent(user)
        user_data["intent"] = intent

        if intent == "greeting":
            print("Bot: Hi! You can ask about pricing or plans 😊")

        elif intent == "pricing":
            basic = knowledge["pricing"]["basic"]
            pro = knowledge["pricing"]["pro"]

            print("\nBot: Here are our plans 👇\n")

            print("Basic Plan:")
            print(f"- {basic['price']}")
            print(f"- {basic['videos']}")
            print(f"- {basic['quality']}\n")

            print("Pro Plan:")
            print(f"- {pro['price']}")
            print(f"- {pro['videos']}")
            print(f"- {pro['quality']}")
            print(f"- {pro['extras']}")

        elif intent == "refund":
            print("Bot:", knowledge["policies"]["refund"])
        elif intent == "ack":
            print("Bot: 👍 Let me know if you’d like to proceed or explore a plan.")

        elif intent == "support":
            print("Bot:", knowledge["policies"]["support"])

        elif intent == "high_intent":
            print("Bot: Great! Let's get you signed up.")

            if not user_data["name"]:
                user_data["name"] = input("Bot: What's your name? ")

            if not user_data["email"]:
                user_data["email"] = input("Bot: Your email? ")

            if not user_data["platform"]:
                user_data["platform"] = input("Bot: Your platform (YouTube/Instagram/others)? ")

            mock_lead_capture(
                user_data["name"],
                user_data["email"],
                user_data["platform"]
            )
            break

        else:
            print("Bot: Sorry, I didn't understand.")


chatbot()
