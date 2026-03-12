PAGE_TITLE = "Exercise 2 — Financial Insight Generator"
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


st.markdown("Paste a short financial report, earnings summary, or business update.")

report_text = st.text_area("Financial text", height=250, placeholder="Paste report text here...")
target_reader = st.text_input("Target reader", value="a non-finance manager")

if st.button("Generate insights"):
    if not report_text.strip():
        st.warning("Please paste financial text first.")
    else:
        prompt = f"""
Analyze this financial report for {target_reader}.

Provide:
1. Key trends
2. Financial risks
3. Strategic insights
4. A simple explanation for non-experts
5. One note on how AI reduces the cost of producing this kind of intelligence

Financial text:
{report_text}
"""
        with st.spinner("Generating insights..."):
            result = run_prompt(prompt)
        st.subheader("Output")
        st.write(result)
