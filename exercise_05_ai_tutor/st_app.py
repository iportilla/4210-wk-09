PAGE_TITLE = "Exercise 5 — AI Personalized Tutor"
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


st.markdown("Use an LLM to generate tailored teaching content for a specific learner and topic.")

col1, col2 = st.columns([2,1])

with col1:
    topic = st.text_input("Topic", value="AI-enabled vs AI-native business models")
    learner_background = st.text_area(
        "Learner background",
        height=140,
        placeholder="Describe the learner..."
    )

with col2:
    difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"], index=0)
    output_mode = st.selectbox("Output mode", ["Lesson", "Coaching", "Practice session"], index=0)

if st.button("Generate tutoring content", use_container_width=True):
    prompt = f"""
Create a personalized {output_mode} for this topic: {topic}

Difficulty:
{difficulty}

Learner background:
{learner_background}

Provide:
1. Explanation
2. Two examples
3. Three practice questions
4. Brief feedback tips
5. Business Insight: How does this demonstrate scalable personalization?

Make the tone encouraging and educational.
"""
    with st.spinner("Generating tutor content..."):
        result = st_run_prompt(prompt, DEFAULT_SYSTEM)
    st.subheader("Tutoring Output")
    st.write(result)

st.divider()
st.info("Reflection: What human service is being scaled here, and what still requires human expertise?")
