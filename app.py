import streamlit as st
import requests
import os

st.set_page_config(page_title="Quick Pitch", layout="centered")

st.title("Quick Pitch – Startup Idea Validator")

# Your Input
st.subheader("Your Idea")
problem = st.text_area("🔍 What's the problem you are looking to solve?", height=120)
solution = st.text_area("💡 What's your solution?", height=120)
roast_mode = st.checkbox("🔥 Enable Roast Mode")

# Submit button
submitted = st.button("Pitch It!")

# Prompt generator
def build_prompt(problem, solution, roast_mode):
    roast_section = (
        "The Roast 🔥:\n    - Roast in a humorous tone. Keep it short and punchy"
        if roast_mode else ""
    )
    return f"""
You are a startup coach. Your task is to evaluate a startup idea with clarity and structure.

Strict instructions:
- Do NOT include preambles or markdown.
- Follow this exact format:

Honest Feedback:
    - Success Probability: Choose one [Low (0–25%), Fair (25–50%), High (50–75%), Very High (>75%)]
    - Validation Verdict: [Good idea / Viable with refinement / Weak idea]
    - Key Areas to Focus: Short bullets

SWOT Analysis:
    - Strengths: ...
    - Weaknesses: ...
    - Opportunities: ...
    - Threats: ...

TAM Estimate:
    - Estimated Market Size: Dollar estimate + 1-line logic

Final Summary:
    - Analytical summary with a clear go/no-go

{roast_section}

Startup Idea:
- Problem: {problem}
- Solution: {solution}
"""

# Model config list
MODEL_CONFIGS = [
    {
        "name": "llama3-70b-8192",
        "provider": "groq",
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "api_key": st.secrets["GROQ_API_KEY"],
        "headers": {
            "Authorization": f"Bearer {st.secrets["GROQ_API_KEY"]}",
            "Content-Type": "application/json"
        }
    },
    {
        "name": "llama3-8b-8192",
        "provider": "groq",
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "api_key": st.secrets["GROQ_API_KEY"],
        "headers": {
            "Authorization": f"Bearer {st.secrets["GROQ_API_KEY"]}",
            "Content-Type": "application/json"
        }
    },
    {
        "name": "llama-3.1-8b-instant",
        "provider": "groq",
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "api_key": st.secrets["GROQ_API_KEY"],
        "headers": {
            "Authorization": f"Bearer {st.secrets["GROQ_API_KEY"]}",
            "Content-Type": "application/json"
        }
    }
]

# Model fallback handler
def call_model(prompt, config):
    payload = {
        "model": config["name"],
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    res = requests.post(config["url"], headers=config["headers"], json=payload)
    res.raise_for_status()
    return res.json()['choices'][0]['message']['content']

# Generate and show output
if submitted:
    if not problem or not solution:
        st.warning("Please enter both a problem and a solution.")
    else:
        with st.spinner("Thinking..."):
            prompt = build_prompt(problem, solution, roast_mode)

            for config in MODEL_CONFIGS:
                try:
                    response = call_model(prompt, config)
                    st.subheader("📊 Your Idea Analysed")
                    st.text_area("", response, height=500)
                    break
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        continue
                    else:
                        print(f"Model {model_config['name']} failed with {code}: {e.response.text}")
            else:
                st.error("AI model generation limit reached. Please try again later.")