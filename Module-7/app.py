import streamlit as st
from retriever import Retriever
from agent import Agent
from llm import generate_response
from evaluator import Evaluator

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Multi-Domain GenAI Assistant", page_icon="🤖")

st.title("🤖 Domain-Specific GenAI Assistant")
st.write("Select a domain and ask your question.")

# -----------------------------
# Domain Dropdown (Main Feature)
# -----------------------------
domain_files = {
    "Placement Assistant": "data/placement.txt",
    "Academic Assistant": "data/academic.txt",
    "Research Paper Explainer": "data/research.txt",
    "Coding Debug Assistant": "data/coding.txt",
    "Startup Idea Evaluator": "data/startup.txt"
}

selected_domain = st.selectbox(
    "Choose Domain",
    options=list(domain_files.keys())
)

st.markdown(f"**Selected Domain:** {selected_domain}")

# -----------------------------
# Load Components Based on Domain
# -----------------------------
@st.cache_resource
def load_retriever(file_path):
    return Retriever(file_path)

retriever = load_retriever(domain_files[selected_domain])
agent = Agent()
evaluator = Evaluator()

# -----------------------------
# User Question Input
# -----------------------------
query = st.text_input(f"Ask your question related to {selected_domain}:")

if st.button("Generate Answer"):

    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):

            # Step 1: Retrieve domain-specific context
            retrieved_docs = retriever.retrieve(query)

            # Step 2: Agent creates structured prompt
            prompt = agent.create_prompt(query, retrieved_docs)

            # Step 3: LLM generates answer
            response = generate_response(prompt)

            # Step 4: Evaluate response
            evaluation = evaluator.evaluate(query, response)

        # -----------------------------
        # Display Results
        # -----------------------------
        st.subheader("📌 Final Answer")
        st.write(response)

        st.subheader("📊 Evaluation Score")
        st.metric("Score ( /100 )", evaluation["score_out_of_100"])
        # Progress bar
        confidence = evaluation["score_out_of_100"] / 100
        st.progress(confidence)

        st.subheader("📚 Retrieved Context")
        for doc in retrieved_docs:
            st.write("•", doc)