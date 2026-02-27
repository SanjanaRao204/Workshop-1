from retriever import Retriever
from agent import Agent
from llm import generate_response
from evaluator import Evaluator

def main():
    retriever = Retriever("data/knowledge.txt")
    agent = Agent()
    evaluator = Evaluator()

    query = input("Ask your question: ")

    # Step 1: Retrieve relevant context
    retrieved_docs = retriever.retrieve(query)

    # Step 2: Agent creates structured prompt
    prompt = agent.create_prompt(query, retrieved_docs)

    # Step 3: LLM generates answer
    response = generate_response(prompt)

    # Step 4: Evaluate response
    evaluation = evaluator.evaluate(query, response)

    print("\n===== FINAL ANSWER =====\n")
    print(response)

    print("\n===== EVALUATION =====\n")
    print(evaluation)

if __name__ == "__main__":
    main()