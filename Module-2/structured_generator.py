from dotenv import load_dotenv
from groq import Groq
import os
import json
from prompts import build_prompt

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(topic: str, temperature: float = 0.0):
    """
    Generates structured JSON response.
    Default temperature = 0.0 for deterministic output.
    """

    prompt = build_prompt(topic)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You generate strictly valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    output = response.choices[0].message.content.strip()

    # Validate JSON
    try:
        parsed = json.loads(output)
        return json.dumps(parsed, indent=4)
    except json.JSONDecodeError:
        return json.dumps({
            "error": "Model did not return valid JSON",
            "raw_output": output
        }, indent=4)


if __name__ == "__main__":
    topic = input("Enter topic: ")
    
    # Force deterministic default
    temperature_input = input("Enter temperature (Press Enter for 0.0): ")
    temperature = float(temperature_input) if temperature_input else 0.0

    print("\n--- AI OUTPUT ---\n")
    print(generate_response(topic, temperature))
    