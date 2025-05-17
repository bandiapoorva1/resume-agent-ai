
# 🧠 AI Resume Critique & Enhancement Agent

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-success)](https://openai.com/)
[![Gradio UI](https://img.shields.io/badge/Gradio-Interface-green)](https://gradio.app/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

> A fully agentic AI system that parses, critiques, and enhances resumes using LLMs and RAG (Retrieval-Augmented Generation). Ideal for job seekers to tailor resumes smartly for any role.

---

## 🚀 Features

- 📄 Upload a resume (PDF or DOCX)
- 🔍 Parses the resume and identifies key sections
- 🧠 Critiques the resume using GPT-4
- 🛠 Enhances weak sections with stronger language and metrics
- 🎯 Optionally tailors to a job description using RAG
- 🧑‍💻 Chat-based interface powered by Gradio

---

## 🗂️ Project Structure

```
resume-agent/
├── main.py                # Entry point to launch the app
├── resume_parser.py       # Resume parsing logic
├── critique_agent.py      # LLM-based resume critique logic
├── enhancement_agent.py   # LLM-based resume rewriting logic
├── rag_module.py          # Job description tailoring using RAG
├── app_ui.py              # Gradio app UI (rename to app.py if using HF Spaces)
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
└── sample_resume.pdf      # Test resume file
```

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/resume-agent-ai.git
cd resume-agent-ai
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python main.py
```

This will launch a local Gradio UI where you can:
- Upload your resume
- Enter a job description (optional)
- Get critique + improved version + tailored version

---

## 🧠 How It Works

1. **Parsing**: `pyresparser` extracts sections like education, experience, skills.
2. **Critiquing**: GPT-4 provides bullet-point feedback on resume quality.
3. **Enhancing**: GPT-4 rewrites selected sections to use metrics and action words.
4. **Tailoring**: If a job description is provided, it embeds it and matches it with resume content using RAG.
5. **User Interface**: All this is wrapped into an intuitive Gradio-powered UI.

---

## 🌐 One-Click Deploy

### Option 1: [Hugging Face Spaces](https://huggingface.co/spaces)

1. Create a Hugging Face account
2. Create a new Space (SDK = Gradio)
3. Upload this project or push it via Git
4. Rename `app_ui.py` to `app.py`

### Option 2: [Streamlit Cloud](https://streamlit.io/cloud)

1. Connect your GitHub repo
2. Point to `app_ui.py` as entry file
3. Click “Deploy”

---

## 🏷️ Tags

```
agentic-ai, resume-enhancer, openai-gpt4, gradio-app, langchain, ai-resume-critiquer, ats-friendly, llm-project, job-search-tools, fullstack-ai
```

---

## ✨ Sample Output

- **Critique**:
    > Your experience section lacks quantifiable impact. Try converting passive phrases into metric-driven actions.

- **Enhanced**:
    > Led a cross-functional team of 5 to develop a web application, increasing onboarding speed by 30%.

- **Tailored** (for a Data Scientist job):
    > Emphasized Python-based data pipelines, ML model deployment, and business impact of analytics.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♀️ Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change or improve.

---

## 🧑‍💼 Maintainer

**Apoorva Bandi**  
[GitHub Profile](https://github.com/bandiapoorva)
