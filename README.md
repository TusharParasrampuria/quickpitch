# QuickPitch – Startup Idea Validator

QuickPitch is a lightweight Streamlit app that helps entrepreneurs and innovators validate their startup ideas instantly. Just input your problem and solution, and get a sharp evaluation including:

- Honest feedback with a success probability
- SWOT analysis
- TAM estimate with breakdown
- Optional roast mode for humorous critique
- Final analytical summary verdict

---

## 🧠 Powered by

- **Streamlit** — for the interactive UI
- **Groq** — for blazing fast LLM-powered insights
- **Dynamic model fallback** — uses multiple models automatically if one fails

---

## 📦 Features

- Minimal, clean UI (mobile-friendly)
- Prompt structure optimized for clarity, realism, and direct advice
- No markdown or fluff — just facts, structure, and a verdict
- Deploy-ready in minutes

---

## 🚀 How to Run

### 🔧 Local (for testing or development)

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/quickpitch.git
   cd quickpitch
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your API keys in .env:
    ```toml
    GROQ_API_KEY=your-groq-api-key
    ```

4. Run the app:
    ```bash
    streamlit run quickpitch_app.py
    ```

# 🌐 Deploy to Streamlit Cloud
1. Push the repo to GitHub
2. Go to https://streamlit.io/cloud
3. Click New App → Connect to GitHub → Select quickpitch_app.py
4. Add the following Secrets in Settings:
    ```toml
    GROQ_API_KEY = your-key-here
    OPENROUTER_API_KEY = your-key-here
    ```
5. Click Deploy — you're live in seconds

## 🔐 Requirements
* Python 3.7+
* API keys for outreach generation:
    * Groq: https://console.groq.com 