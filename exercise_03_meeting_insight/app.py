PAGE_TITLE = "Exercise 3 — Meeting Insight Generator"
CAPTION = "Theme: Speed of Analysis"


import os, sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import run_prompt

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Paste meeting notes and extract decisions, actions, and risks.")

meeting_notes = st.text_area("Meeting notes", height=250, placeholder="Paste notes here...")
meeting_type = st.text_input("Meeting type", value="project planning")

if st.button("Summarize meeting"):
    if not meeting_notes.strip():
        st.warning("Please paste meeting notes first.")
    else:
        prompt = f"""
Analyze these {meeting_type} meeting notes.

Provide:
1. Decisions made
2. Action items with owners if visible
3. Unresolved questions
4. Potential risks
5. One note on how this changes the speed of organizational coordination

Meeting notes:
{meeting_notes}
"""
        with st.spinner("Extracting insights..."):
            result = run_prompt(prompt)
        st.subheader("Output")
        st.write(result)
