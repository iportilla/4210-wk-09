PAGE_TITLE = "Exercise 5 — AI Personalized Tutor"
CAPTION = "Theme: Scale of Personalized Services"


import os, sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "shared"))

from llm_utils import run_prompt

st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)
st.caption(CAPTION)


st.markdown("Generate personalized teaching material for a topic.")

topic = st.text_input("Topic", value="Business model innovation")
level = st.selectbox("Difficulty level", ["Beginner", "Intermediate", "Advanced"], index=1)
goal = st.text_input("Learning goal", value="understand AI-enabled vs AI-native business models")

if st.button("Generate tutor output"):
    prompt = f"""
Teach the concept: {topic}

Difficulty level: {level}
Learning goal: {goal}

Provide:
1. A clear explanation
2. Two examples
3. Three practice questions
4. Brief feedback tips for a student
5. One note on how AI enables personalized services at scale
"""
    with st.spinner("Generating tutoring content..."):
        result = run_prompt(prompt)
    st.subheader("Output")
    st.write(result)
