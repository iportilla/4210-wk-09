PAGE_TITLE = "Exercise 2 — Financial Insight Generator"
CAPTION = "Theme: Cost of Producing Intelligence"


import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import st_run_prompt, DEFAULT_SYSTEM

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Use an LLM to turn raw financial text into trends, risks, and strategic insights.")

col1, col2 = st.columns([2,1])

with col1:
    report_text = st.text_area(
        "Paste financial report excerpt or company performance summary",
        height=260,
        placeholder="Paste a short financial report here..."
    )

with col2:
    reader = st.selectbox("Target reader", ["Non-finance manager", "Founder", "Student", "Investor"], index=0)
    format_type = st.selectbox("Output style", ["Bullet summary", "Executive memo", "Simple explanation"], index=0)

if st.button("Generate financial insights", use_container_width=True):
    if not report_text.strip():
        st.warning("Please paste financial text first.")
    else:
        prompt = f"""
Analyze this financial report for a {reader}.
Format the response as a {format_type}.

Provide:
1. Key Trends
2. Financial Risks
3. Strategic Insights
4. Plain English Explanation
5. Business Insight: Why does this lower the cost of producing intelligence?

Financial text:
{report_text}
"""
        with st.spinner("Generating insights..."):
            result = st_run_prompt(prompt, DEFAULT_SYSTEM)
        st.subheader("Analysis")
        st.write(result)

st.divider()
st.info("Reflection: Which jobs or workflows depend heavily on expert interpretation of financial information?")
