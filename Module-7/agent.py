class Agent:
    def __init__(self):
        pass

    def create_prompt(self, query, retrieved_docs):
        context = "\n".join(retrieved_docs)

        prompt = f"""
You are a Placement Preparation Assistant.

Use the provided context to answer the question.

Context:
{context}

User Question:
{query}

Provide a structured answer with:
1. Explanation
2. Key Points
3. Actionable Advice
"""
        return prompt