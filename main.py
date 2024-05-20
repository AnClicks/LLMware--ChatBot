import streamlit as st
from llmware.prompts import Prompt

# Configure Streamlit page settings
st.set_page_config(
    page_title=" LLMware ChatBot",
    page_icon="💬",
    layout="centered"
)

# Streamlit page title
st.title("🤖 LLMWare powered - ChatBot")

# Input field for user's message
user_prompt = st.text_input("Ask your doubts...")

if user_prompt:
    # Load LLMware model
    LLMWARE_MODEL_NAME = "phi-3-gguf"
    model = Prompt().load_model(LLMWARE_MODEL_NAME)

    # Send user's message to LLMware model and get a response
    output = model.prompt_main(
        user_prompt,
        prompt_name="default_with_context",
        temperature=0.7
    )
    assistant_response = output["llm_response"].strip("\n").replace("<|end|>", "").replace("<|assistant|>", "")

    # Display LLMware's response
    st.write("👤 You:", user_prompt)
    st.write("🤖 Assistant:", assistant_response)
