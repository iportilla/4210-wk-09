PAGE_TITLE = "Exercise 1 — AI Policy Explainer"
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


st.markdown("Paste a policy, legal clause, or guideline. The app will explain it in plain language.")

policy_text = st.text_area("Policy text", height=250, placeholder="Paste policy text here...")
audience = st.text_input("Audience", value="students or non-experts")

if st.button("Explain policy"):
    if not policy_text.strip():
        st.warning("Please paste policy text first.")
    else:
        prompt = f"""
Explain the following policy in plain language for {audience}.

Provide:
1. A short summary
2. Key requirements
3. Potential risks if misunderstood or violated
4. Recommended actions
5. One sentence on what business or professional service this could automate or reduce in cost

Policy:
{policy_text}
"""
        with st.spinner("Analyzing..."):
            result = run_prompt(prompt)
        st.subheader("Output")
        st.write(result)
