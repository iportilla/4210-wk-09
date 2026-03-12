PAGE_TITLE = "Exercise 3 — Meeting Insight Generator"
CAPTION = "Theme: Speed of Analysis"


import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import st_run_prompt, DEFAULT_SYSTEM

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Use an LLM to turn meeting notes into decisions, actions, risks, and next steps.")

col1, col2 = st.columns([2,1])

with col1:
    meeting_notes = st.text_area(
        "Paste meeting notes or transcript excerpt",
        height=260,
        placeholder="Paste meeting notes here..."
    )

with col2:
    meeting_type = st.selectbox("Meeting type", ["Project planning", "Client meeting", "Strategy meeting", "Team sync"], index=0)
    audience = st.selectbox("Summary audience", ["Team members", "Manager", "Executives"], index=0)

if st.button("Summarize meeting", use_container_width=True):
    if not meeting_notes.strip():
        st.warning("Please paste meeting notes first.")
    else:
        prompt = f"""
Analyze these {meeting_type} notes for {audience}.

Provide:
1. Decisions Made
2. Action Items
3. Unresolved Questions
4. Potential Risks
5. Suggested Next Steps
6. Business Insight: How does this increase the speed of analysis and coordination?

Meeting notes:
{meeting_notes}
"""
        with st.spinner("Extracting insights..."):
            result = st_run_prompt(prompt, DEFAULT_SYSTEM)
        st.subheader("Meeting Summary")
        st.write(result)

st.divider()
st.info("Reflection: How does faster meeting synthesis change team coordination or management overhead?")
