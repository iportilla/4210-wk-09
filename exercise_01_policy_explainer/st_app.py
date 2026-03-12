PAGE_TITLE = "Exercise 1 — AI Policy Explainer"
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


st.markdown("Use an LLM to translate complex policy text into plain language, risks, and actions.")

col1, col2 = st.columns([2,1])

with col1:
    policy_text = st.text_area(
        "Paste policy, legal, or compliance text",
        height=260,
        placeholder="Paste policy text here..."
    )

with col2:
    audience = st.selectbox("Audience", ["Students", "Managers", "General Public", "Non-experts"], index=0)
    tone = st.selectbox("Tone", ["Clear and practical", "Formal", "Friendly"], index=0)

if st.button("Explain policy", use_container_width=True):
    if not policy_text.strip():
        st.warning("Please paste policy text first.")
    else:
        prompt = f"""
Explain the following policy for this audience: {audience}
Use this tone: {tone}

Provide these sections with headings:
1. Plain Language Summary
2. Key Requirements
3. Risks if Misunderstood or Violated
4. Recommended Actions
5. Business Insight: What professional service or task becomes cheaper because of a system like this?

Policy text:
{policy_text}
"""
        with st.spinner("Analyzing policy..."):
            result = st_run_prompt(prompt, DEFAULT_SYSTEM)
        st.subheader("Analysis")
        st.write(result)

st.divider()
st.info("Reflection: What expert work did this system partially automate?")
