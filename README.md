# 🛡️ PhishGuard — AI Phishing Message & URL Analyzer

> **AI-powered cybersecurity application for detecting, analyzing, and explaining potential phishing and social-engineering threats.**

PhishGuard is a defensive cybersecurity application that analyzes suspicious **messages and URLs** using rule-based security checks, heuristic risk scoring, **RAG (Retrieval-Augmented Generation)**, **FAISS**, **LangChain**, and **Hugging Face LLMs**.

Instead of simply providing a risk score, PhishGuard explains **why content may be suspicious**, identifies security indicators, retrieves relevant cybersecurity knowledge, and provides safe defensive recommendations.

🚀 **Built for the HackDevengers 24-Hour Hackathon**

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
                     │ Assessment            │
                     │ + Recommendations     │
                     └──────────────────────┘
```

---

# 🏗️ Architecture

```text
┌─────────────────────────────┐
│       Streamlit UI          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Message / URL Input    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Python Analyzer       │
│       Rule-Based Checks     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Risk Score + Signals   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       RAG Retriever         │
│       FAISS Vector Store    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Knowledge Base        │
│        TXT Documents        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       LangChain + LLM       │
│        Hugging Face         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Security Explanation    │
│     + Safe Recommendation   │
└─────────────────────────────┘
```

---

# 📁 Project Structure

```text
PhishGuard/
│
├── app.py
├── analyzer.py
├── llm_analyzer.py
├── rag.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── knowledge/
│   ├── phishing.txt
│   ├── social_engineering.txt
│   ├── suspicious_urls.txt
│   └── cybersecurity_safety.txt
│
└── vectorstore/
    ├── index.faiss
    └── index.pkl
```

### 📄 File Description

| File / Folder | Purpose |
|---|---|
| `app.py` | Streamlit user interface and dashboard |
| `analyzer.py` | Rule-based message and URL analysis |
| `llm_analyzer.py` | LangChain + Hugging Face LLM integration |
| `rag.py` | RAG pipeline and FAISS vector store |
| `knowledge/` | Local cybersecurity knowledge base |
| `vectorstore/` | Generated FAISS vector index |
| `requirements.txt` | Python dependencies |
| `.env` | Local environment variables |
| `.gitignore` | Files excluded from Git |
| `README.md` | Project documentation |

> ⚠️ **Note:** `vectorstore/` is generated automatically and should normally be excluded from GitHub.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| LLM Framework | LangChain |
| LLM Provider | Hugging Face |
| RAG | Retrieval-Augmented Generation |
| Vector Store | FAISS |
| Embeddings | Sentence Transformers |
| Knowledge Base | Local TXT Files |
| Environment Management | python-dotenv |

---

## 📊 Risk Classification

| Score | Risk Level |
|---:|---|
| 0–39 | 🟢 LOW |
| 40–69 | 🟠 MEDIUM |
| 70–100 | 🔴 HIGH |

> ⚠️ The risk score is a **heuristic security indicator**, not a calibrated probability or proof that content is malicious.

---

## 🔐 Security Approach

PhishGuard is designed for **defensive cybersecurity analysis**.

The system:

- ✅ Analyzes existing suspicious content
- ✅ Identifies potential phishing indicators
- ✅ Uses cybersecurity knowledge for contextual analysis
- ✅ Provides defensive recommendations
- ❌ Does not generate phishing messages
- ❌ Does not provide instructions for conducting phishing
- 🛡️ Warns users against sharing passwords and OTPs
- 🔒 Treats user-provided content as untrusted data during AI analysis

---

## ⚠️ Limitations

PhishGuard is a prototype developed for **educational and hackathon purposes**.

Current limitations include:

- Rule-based detection can produce false positives and false negatives.
- Risk scores are heuristic rather than calibrated probabilities.
- LLM responses can vary between requests.
- URL analysis does not prove that a website is malicious.
- HTTPS does not guarantee that a website is safe.
- The system should not replace professional cybersecurity tools.
- Model availability and Hugging Face provider support may vary.

---

## 🔮 Future Enhancements

- 🌐 Real-time threat intelligence APIs
- 🔎 Domain reputation analysis
- 🌍 WHOIS and DNS analysis
- 🔤 Typosquatting detection
- 📱 QR-code phishing detection
- 📧 Email header analysis
- 🌐 Browser extension
- 🗣️ Multilingual phishing detection
- 🧠 ML-based phishing classification
- 📚 Expanded cybersecurity RAG knowledge base
- 📈 Advanced explainable-AI visualizations
- 👥 User feedback and reporting system
- 🔐 Additional security verification signals

---

# 🏆 Hackathon

| Detail | Information |
|---|---|
| 🚀 Project | **PhishGuard — AI Phishing Message & URL Analyzer** |
| 🏆 Event | **HackDevengers 24-Hour Hackathon** |
| 🔐 Domain | **Cybersecurity + Artificial Intelligence** |
| 🤖 Core Technologies | **Python, LangChain, RAG, FAISS, Hugging Face** |

---

## 👩‍💻 Contributors

Developed as a **team project** for the **HackDevengers 24-Hour Hackathon**.

---

## 📄 License

This project is intended for **educational, research, and hackathon purposes**.

---

<p align="center">
  🛡️ <strong>PhishGuard</strong> — Detect. Explain. Protect.
</p>

<p align="center">
  Built with ❤️ using Python, LangChain, RAG, FAISS & Hugging Face
</p>