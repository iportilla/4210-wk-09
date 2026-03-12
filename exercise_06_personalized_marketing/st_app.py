PAGE_TITLE = "Exercise 6 — Personalized Marketing Generator"
CAPTION = "Theme: Scale of Personalized Services"


import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import st_run_prompt, DEFAULT_SYSTEM

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Use an LLM to create personalized marketing content for a product and customer persona.")

col1, col2 = st.columns([2,1])

with col1:
    product = st.text_input("Product", value="AI study assistant for business students")
    persona = st.text_area(
        "Customer persona",
        height=180,
        placeholder="Describe the customer persona..."
    )

with col2:
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Bold", "Educational"], index=0)
    channel = st.selectbox("Primary channel", ["Email", "LinkedIn", "Instagram", "Website"], index=0)

if st.button("Generate marketing content", use_container_width=True):
    if not persona.strip():
        st.warning("Please describe the customer persona first.")
    else:
        prompt = f"""
Create personalized marketing content.

Product:
{product}

Customer persona:
{persona}

Tone:
{tone}

Primary channel:
{channel}

Provide:
1. A short email campaign
2. Ad copy
3. A social media or channel-specific message
4. A one-line value proposition
5. Business Insight: Why does personalization change marketing economics?

Keep the content concise and realistic.
"""
        with st.spinner("Generating marketing assets..."):
            result = st_run_prompt(prompt, DEFAULT_SYSTEM)
        st.subheader("Marketing Output")
        st.write(result)

st.divider()
st.info("Reflection: If personalized messaging becomes cheap, how does that change competition in marketing?")
