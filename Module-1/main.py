from groq import Groq
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

def generate_explanation(topic, style):
    system_prompt = """
    You are an expert teacher.
    Always explain clearly and fully stay in the selected character style.
    """

    user_prompt = f"Explain {topic} in {style} style."

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content


# ---- Main Program ----
print("🎭 Prompt-Based Style Explainer")
print("Choose style: Shakespeare / Pirate / Bandit")

topic = input("Enter topic: ")
style = input("Enter style: ")

output = generate_explanation(topic, style)

print("\n--- AI Explanation ---\n")
print(output)