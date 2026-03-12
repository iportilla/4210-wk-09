PAGE_TITLE = "Exercise 0 — Preparation"
CAPTION = "Theme: Cost of Producing Intelligence"


import os, sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import run_prompt

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("The app will chat with you.")

chat_text = st.text_area("Chat text", height=250, placeholder="Type your message here...")
audience = st.text_input("Audience", value="students or non-experts")

if st.button("Answer"):
    if not chat_text.strip():
        st.warning("Please type your message first.")
    else:
        prompt = f"""
Chat in plain language for {audience}.

Provide:
- A concise answer to the question.
- A brief explanation of the answer.

Question:
{chat_text}
"""
        with st.spinner("Analyzing..."):
            result = run_prompt(prompt)
        st.subheader("Output")
        st.write(result)
