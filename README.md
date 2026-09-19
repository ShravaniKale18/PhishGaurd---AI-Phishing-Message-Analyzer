# 🛡️ PhishGuard — AI Phishing Message & URL Analyzer

> **AI-powered cybersecurity application for detecting, analyzing, and explaining potential phishing and social-engineering threats.**

PhishGuard is a defensive cybersecurity application that analyzes suspicious **messages and URLs** using rule-based security checks, heuristic risk scoring, **RAG (Retrieval-Augmented Generation)**, **FAISS**, **LangChain**, and **Hugging Face LLMs**.

Instead of simply providing a risk score, PhishGuard explains **why content may be suspicious**, identifies security indicators, retrieves relevant cybersecurity knowledge, and provides safe defensive recommendations.

🚀 **Built for the HackDevengers 24-Hour Hackathon**

### 🌐 Live Demo

👉 **[Launch PhishGuard](https://phishgaurd---ai-phishing-message-analyzer-b5aw8qqdualgw83rnvkk.streamlit.app/)**

---

## ✨ Features

- 🔍 Analyze suspicious messages
- 🔗 Analyze suspicious URLs
- ⚠️ Detect urgency and pressure tactics
- 🔐 Detect credential requests
- 🔑 Detect OTP requests
- 💳 Detect financial information requests
- 🚨 Detect account suspension/threat messages
- 🌐 Analyze suspicious URL characteristics
- 📊 Generate a heuristic risk score from **0–100**
- 🟢 **LOW** / 🟠 **MEDIUM** / 🔴 **HIGH** risk classification
- 🧠 RAG-based cybersecurity knowledge retrieval
- 🤖 AI-powered security explanations
- 🛡️ Defensive security recommendations
- 💻 Interactive Streamlit dashboard
- 🔒 Local cybersecurity knowledge base
- ⚡ FAISS-powered similarity search

---

# 🧠 How It Works

PhishGuard combines deterministic security checks with AI-powered contextual analysis.

```text
                     ┌──────────────────────┐
                     │      User Input      │
                     │    Message / URL     │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │  Rule-Based Analyzer │
                     │                      │
                     │ • Keywords           │
                     │ • Urgency            │
                     │ • OTP / Credentials  │
                     │ • Financial Requests │
                     │ • URL Characteristics│
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Risk Score + Signals │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │    RAG Retriever     │
                     │    FAISS Vector      │
                     │       Store          │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │   Cybersecurity      │
                     │   Knowledge Base     │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │    LangChain + LLM   │
                     │    Hugging Face      │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Explainable Security │
                     │ Assessment           │
                     │ + Recommendations    │
                     └──────────────────────┘
