PAGE_TITLE = "Exercise 4 — Market Research Assistant"
CAPTION = "Theme: Speed of Decision Support"


import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import st_run_prompt, DEFAULT_SYSTEM

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Use an LLM to generate a rapid market scan for a product idea.")

col1, col2 = st.columns([2,1])

with col1:
    product_idea = st.text_area(
        "Describe the product or startup idea",
        height=220,
        placeholder="Describe your product idea..."
    )

with col2:
    target_market = st.text_input("Target market", value="small business owners")
    geography = st.text_input("Geography", value="US")
    stage = st.selectbox("Stage", ["Idea", "MVP", "Growth"], index=0)

if st.button("Analyze market", use_container_width=True):
    if not product_idea.strip():
        st.warning("Please describe the product idea first.")
    else:
        prompt = f"""
Analyze the market opportunity for this product idea.

Product idea:
{product_idea}

Target market:
{target_market}

Geography:
{geography}

Stage:
{stage}

Provide:
1. Likely Competitors
2. Differentiation Opportunities
3. Key Risks
4. Possible Customer Value
5. Suggested Next Questions
6. Business Insight: How does this speed up decision support?

Use concise startup language.
"""
        with st.spinner("Analyzing market..."):
            result = st_run_prompt(prompt, DEFAULT_SYSTEM)
        st.subheader("Market Analysis")
        st.write(result)

st.divider()
st.info("Reflection: What strategic work became faster because the LLM generated a first-pass market scan?")
