🏗 Module 3 — LLM Application Architecture

This project demonstrates how to design a modular LLM application pipeline using clean software engineering principles.

Instead of building everything in one script, the system is structured into layers:

User Input → Prompt Layer → LLM Layer → Post-Processing → Output

🎯 Objective

Build a scalable, production-style LLM workflow with clear separation of responsibilities.

🧠 Key Concepts

Modular AI system design

Separation of concerns

Prompt abstraction layer

Model invocation layer (Groq via LiteLLM)

Output post-processing

📂 Project Structure
module3_architecture/
│
├── input_layer.py
├── prompt_layer.py
├── llm_layer.py
├── post_processing.py
├── pipeline.py
├── requirements.txt
└── .env.example
⚙ Setup
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

Create a .env file:

GROQ_API_KEY=your_key_here
MODEL_NAME=groq/llama-3.1-8b-instant

Run the project:

python pipeline.py
🚀 Why This Matters

Real-world AI systems are modular pipelines — not single scripts.
This project builds the engineering mindset required to design scalable GenAI applications.