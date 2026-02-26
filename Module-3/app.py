import streamlit as st
from prompt_layer import build_prompt
from llm_layer import call_llm
from post_processing import clean_output

st.set_page_config(page_title="Module 3 LLM Architecture")

st.title("🏗 Modular LLM Architecture")
st.write("Ask any academic question below:")

user_input = st.text_input("Enter your question")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Generating response..."):
            prompt = build_prompt(user_input)
            raw_output = call_llm(prompt)
            final_output = clean_output(raw_output)

        st.success("AI Response")
        st.write(final_output)
    else:
        st.warning("Please enter a question.")