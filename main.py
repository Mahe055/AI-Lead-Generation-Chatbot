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

# Load document
loader = TextLoader("knowledge.txt")
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)
print("Loaded docs:", len(docs))

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
    print("DEBUG INPUT:", user_input_lower)

    if any(word in user_input_lower for word in ["hi", "hello", "hey"]):
        print("MATCH: greeting")
        return "greeting"

    if any(word in user_input_lower for word in ["buy", "want", "purchase", "subscribe"]):
        print("MATCH: high_intent")
        return "high_intent"

    if any(word in user_input_lower for word in ["price", "pricing", "cost", "plan"]):
        print("MATCH: pricing")
        return "pricing"

    print("FALLBACK TO LLM")

    try:
        response = llm.invoke(f"Classify intent: {user_input}")
        print("LLM RESPONSE:", response.content)
        intent = response.content.strip().lower()

        if "greeting" in intent:
            return "greeting"
        elif "pricing" in intent:
            return "pricing"
        elif "high" in intent:
            return "high_intent"
        else:
            return "unknown"

    except Exception as e:
        print("ERROR:", e)
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
            with open("knowledge.txt", "r") as f:
                data = f.read()
            print("Bot: Here are our plans 👇")
            print(data)

        elif intent == "high_intent":
            print("Bot: Great! Let's get you signed up.")

            if not user_data["name"]:
                user_data["name"] = input("Bot: What's your name? ")

            if not user_data["email"]:
                user_data["email"] = input("Bot: Your email? ")

            if not user_data["platform"]:
                user_data["platform"] = input("Bot: Your platform (YouTube/Instagram)? ")

            mock_lead_capture(
                user_data["name"],
                user_data["email"],
                user_data["platform"]
            )
            break

        else:
            print("Bot: Sorry, I didn't understand.")


chatbot()