# Page metadata displayed in browser tab and header
PAGE_TITLE = "Exercise 0 — Preparation"
CAPTION = "Theme: Cost of Producing Intelligence"


import os, sys
from pathlib import Path
import streamlit as st

# Navigate to project root and add shared/ to Python path
# This allows importing llm_utils from the shared module
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import run_prompt

# Configure Streamlit page settings
st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)

# Instructions for the user
st.markdown("The app will chat with you.")

# Input widgets for user interaction
chat_text = st.text_area("Chat text", height=150, placeholder="Type your message here...")
audience = st.text_input("Audience", value="students or non-experts")

# Button triggers the AI response
if st.button("Answer"):
    # Validate that user entered text
    if not chat_text.strip():
        st.warning("Please type your message first.")
    else:
        # Construct the prompt with audience context and instructions
        # This prompt engineering ensures consistent, audience-appropriate responses
        prompt = f"""
        Answer in plain language for {audience}.

        Provide:
        - A concise answer to the question.
        - A brief explanation of the answer.

        Question:
        {chat_text}
        """
        # Show loading indicator while waiting for API response
        with st.spinner("Analyzing..."):
            result = run_prompt(prompt)
        
        # Display the AI's response
        st.subheader("Output")
        st.write(result)