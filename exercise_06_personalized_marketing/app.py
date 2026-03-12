PAGE_TITLE = "Exercise 6 — Personalized Marketing Generator"
CAPTION = "Theme: Scale of Personalized Services"


import os, sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import run_prompt

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Create personalized marketing content for a product and persona.")

product = st.text_input("Product", value="AI-powered study assistant")
persona = st.text_area("Customer persona", height=140, placeholder="Describe the target customer...")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Bold", "Educational"], index=0)

if st.button("Generate campaign"):
    if not persona.strip():
        st.warning("Please describe the customer persona first.")
    else:
        prompt = f"""
Create personalized marketing content.

Product: {product}
Customer persona: {persona}
Tone: {tone}

Provide:
1. A short email campaign
2. Ad copy
3. A social media message
4. One sentence on why personalization changes marketing economics
"""
        with st.spinner("Generating marketing assets..."):
            result = run_prompt(prompt)
        st.subheader("Output")
        st.write(result)
