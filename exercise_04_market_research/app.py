PAGE_TITLE = "Exercise 4 — Market Research Assistant"
CAPTION = "Theme: Speed of Decision Support"


import os, sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import run_prompt

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Describe a product idea and target market. The app will generate a rapid market scan.")

product_idea = st.text_area("Product idea", height=180, placeholder="Describe the product or service...")
target_market = st.text_input("Target market", value="small business owners")

if st.button("Analyze market"):
    if not product_idea.strip():
        st.warning("Please describe the product idea first.")
    else:
        prompt = f"""
Analyze the market opportunity for this idea.

Product idea:
{product_idea}

Target market:
{target_market}

Provide:
1. Likely competitors
2. Differentiation opportunities
3. Key risks
4. Likely customer value
5. One note on how AI speeds up early-stage strategic analysis

Return the answer in concise business language.
"""
        with st.spinner("Analyzing market..."):
            result = run_prompt(prompt)
        st.subheader("Output")
        st.write(result)
