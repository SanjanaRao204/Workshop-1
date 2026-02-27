Module 5: Introduction to RAG (Retrieval-Augmented Generation)

This project demonstrates a basic RAG (Retrieval-Augmented Generation) pipeline using keyword-based retrieval and LiteLLM for response generation.

The system retrieves relevant information from a local knowledge base and uses it to generate more accurate and context-aware answers.

Setup

Copy .env.example to .env and add your Groq API key.

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py
Project Structure

knowledge_base/
Contains text files used as the retrieval source.

retriever.py
Handles loading documents and performing simple keyword-based retrieval.

llm_layer.py
Manages interaction with the LLM using LiteLLM.

rag_pipeline.py
Orchestrates the retrieval and generation stages.

main.py
Provides an interactive CLI for users to ask questions.