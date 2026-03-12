# ORGN 4210 — Week 09 Streamlit Starters

## Coding with LLMs: AI & Business Models

This package contains **6 Streamlit starter apps**, one for each Week 09 exercise.

## Included Apps

1. `exercise_01_policy_explainer/`
2. `exercise_02_financial_insight/`
3. `exercise_03_meeting_insight/`
4. `exercise_04_market_research/`
5. `exercise_05_ai_tutor/`
6. `exercise_06_personalized_marketing/`

## Setup

clone repo locally with:

```bash
git clone https://github.com/iportilla/4210-wk-09.git
```

Change directories

```bash
cd 4210-wk-09
```
Create a `.env` file in the project root or set environment variables:

```bash
cp env.sample .env
```
```bash
vi .env
```

Add new values:

- `OPENAI_API_KEY`
- `OPENAI_MODEL` (optional, default: `gpt-4.1-mini`)

## Install

```bash
pip install -r requirements.txt
```

## Run an app

```bash
streamlit run exercise_01_policy_explainer/app.py
```

## Teaching Note

These apps are intentionally simple. The point is to help you connect:

- **LLM capability**
- **business value**
- **economic change**

