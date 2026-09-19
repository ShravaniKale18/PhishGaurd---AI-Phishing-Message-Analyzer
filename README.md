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

## 📄 File Description

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

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| 🎨 Frontend | Streamlit |
| ⚙️ Backend | Python |
| 🧠 LLM Framework | LangChain |
| 🤖 LLM Provider | Hugging Face |
| 🔎 RAG | Retrieval-Augmented Generation |
| 🗄️ Vector Store | FAISS |
| 🔤 Embeddings | Sentence Transformers |
| 📚 Knowledge Base | Local TXT Files |
| 🔐 Environment Management | python-dotenv |
| 🧑‍💻 Development | VS Code, Git, GitHub |

---

# 🔍 Detection Pipeline

## 💬 Message Analysis

PhishGuard analyzes messages for:

- ⚠️ Urgency or pressure
- 🚨 Account suspension threats
- 🔐 Credential requests
- 🔑 OTP requests
- 💳 Financial information requests
- 🔗 External links
- 🔎 Suspicious keywords

## 🔗 URL Analysis

PhishGuard checks for:

- 🔒 HTTP instead of HTTPS
- 🌐 IP addresses instead of domain names
- 📏 Unusually long URLs
- 🔎 Suspicious keywords
- 🌐 Excessive subdomains
- `@` characters
- ⚠️ Suspicious URL structures

> **Note:** These characteristics are indicators only and do not prove that a URL is malicious.

---

# 📊 Risk Classification

PhishGuard generates a **heuristic risk score from 0–100**.

| Score | Risk Level |
|---:|---|
| `0–39` | 🟢 LOW |
| `40–69` | 🟠 MEDIUM |
| `70–100` | 🔴 HIGH |

> ⚠️ The risk score is a **heuristic security indicator**, not a calibrated probability or proof that content is malicious.

---

# 🧠 RAG Pipeline

PhishGuard uses **Retrieval-Augmented Generation (RAG)** to provide relevant cybersecurity context to the AI model.

```text
Knowledge Base
      │
      ▼
Text Documents
      │
      ▼
Text Splitting
      │
      ▼
Hugging Face Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Relevant Cybersecurity Knowledge
      │
      ▼
LangChain
      │
      ▼
Hugging Face LLM
      │
      ▼
Security Explanation
```

## 📚 Knowledge Base

```text
knowledge/
├── phishing.txt
├── social_engineering.txt
├── suspicious_urls.txt
└── cybersecurity_safety.txt
```

The knowledge base contains information related to:

- Phishing
- Social engineering
- Suspicious URLs
- Cybersecurity safety practices

---

# 🤖 AI Analysis

The AI receives:

1. User-provided message or URL
2. Rule-based risk score
3. Detected security indicators
4. Relevant cybersecurity knowledge retrieved through RAG

The LLM generates a structured security assessment containing:

```text
Risk Assessment:

Threat Category:

Explanation:

Warning Signs:

Recommended Action:
```

### Two-Layer Analysis

```text
        ┌────────────────────────┐
        │  Rule-Based Analyzer   │
        └────────────┬───────────┘
                     │
             Deterministic
                Signals
                     │
                     ▼
        ┌────────────────────────┐
        │ Risk Score + Indicators│
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │     RAG Retriever      │
        │       + FAISS          │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │   LangChain + LLM      │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ Explainable Assessment │
        │ + Defensive Guidance   │
        └────────────────────────┘
```

The rule-based analyzer provides deterministic security signals, while RAG and the LLM provide contextual explanations and defensive recommendations.

---

# 🧪 Example Test Cases

## 🔴 Suspicious Message

```text
URGENT! Your bank account has been suspended.

Verify your account immediately and provide your OTP
to restore access.
```

Possible indicators:

```text
⚠ Urgency/Pressure detected
⚠ Account threat detected
⚠ OTP request detected
```

---

## 🟠 Financial Scam Example

```text
Your refund is ready. Confirm your bank and payment
details within 24 hours to receive your refund.
```

Possible indicators:

```text
⚠ Urgency/Pressure detected
⚠ Financial information/request detected
```

---

## 🟢 Normal Message

```text
Your college assignment submission deadline has been
extended to Monday. Please submit it through the official
college portal.
```

This should generally produce fewer phishing indicators.

---

# 📊 Example Output

```text
╔══════════════════════════════╗
║       RISK SCORE: 60/100     ║
║       RISK LEVEL: MEDIUM     ║
╚══════════════════════════════╝

INDICATORS FOUND: 3

⚠ Urgency/Pressure detected
⚠ Possible credential request
⚠ OTP request detected
```

### Example AI Response

```text
Risk Assessment:
60/100 — Potential phishing / social engineering

Threat Category:
Potential phishing / social engineering

Explanation:
Multiple indicators commonly associated with phishing
and social engineering were detected.

Warning Signs:
- Urgency/Pressure detected
- Possible credential request
- OTP request detected

Recommended Action:
Do not provide OTPs or credentials.

Verify the request through the organization's official
website or application.
```

---

# 🔐 Security Approach

PhishGuard is designed specifically for **defensive cybersecurity analysis**.

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

# ⚠️ Limitations

PhishGuard is a prototype developed for **educational and hackathon purposes**.

Current limitations include:

- Rule-based detection can produce false positives and false negatives.
- Risk scores are heuristic rather than calibrated probabilities.
- LLM responses can vary between requests.
- URL analysis does not prove that a website is malicious.
- HTTPS does not guarantee that a website is safe.
- The system should not replace professional cybersecurity tools.
- Model availability and Hugging Face provider support may vary.
- Detection quality depends on the rules and cybersecurity knowledge available to the system.

---

# 🔮 Future Enhancements

Potential improvements include:

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

# ⚙️ Installation

## 1. Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Git
- Hugging Face account/token
- Internet connection

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PhishGuard.git
```

Move into the project directory:

```bash
cd PhishGuard
```

> Replace `YOUR_USERNAME` with your actual GitHub username and use your actual repository URL.

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 5. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 6. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```bash
pip install -U streamlit python-dotenv langchain langchain-core langchain-community langchain-huggingface langchain-text-splitters sentence-transformers faiss-cpu
```

---

# 🔑 Environment Variables

PhishGuard uses a Hugging Face token for LLM integration.

## Create `.env`

Create a file named:

```text
.env
```

in the project root:

```text
PhishGuard/
├── app.py
├── analyzer.py
├── llm_analyzer.py
├── rag.py
└── .env
```

Add:

```env
HF_TOKEN=your_huggingface_token
```

Replace `your_huggingface_token` with your actual Hugging Face access token.

### ⚠️ Never Commit `.env`

Your `.gitignore` should contain:

```gitignore
venv/
.venv/

.env
.env.*

__pycache__/
*.py[cod]

vectorstore/

.streamlit/secrets.toml

.vscode/
.idea/

*.log
```

---

# ▶️ Run the Application

After activating the virtual environment:

```bash
python -m streamlit run app.py
```

The application should open at:

```text
http://localhost:8501
```

You can also run:

```bash
streamlit run app.py
```

---

# 🐛 Troubleshooting

## `streamlit` command not found

Use:

```bash
python -m streamlit run app.py
```

---

## Virtual Environment Is Not Activated

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Command Prompt

```cmd
venv\Scripts\activate
```

---

## PowerShell Execution Policy Error

If PowerShell prevents activation, open **Command Prompt** and run:

```cmd
venv\Scripts\activate
```

Then:

```bash
python -m streamlit run app.py
```

---

## FAISS Vector Store Does Not Exist

The application can create the vector store from the files inside:

```text
knowledge/
```

Generated files:

```text
vectorstore/
├── index.faiss
└── index.pkl
```

If necessary, remove the existing `vectorstore/` directory and run the application again so it can be rebuilt.

---

## Hugging Face Token Error

Check that `.env` exists in the project root:

```text
PhishGuard/
└── .env
```

and contains:

```env
HF_TOKEN=your_huggingface_token
```

Also verify that:

- The token is valid.
- The required model/provider is accessible.
- The environment variables are loaded correctly.

---

# 📌 GitHub Setup

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Create the initial commit:

```bash
git commit -m "Initial commit - PhishGuard"
```

Connect the GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/PhishGuard.git
```

Rename the branch:

```bash
git branch -M main
```

Push:

```bash
git push -u origin main
```

### Verify Your Repository

Your GitHub repository should contain:

```text
PhishGuard/
│
├── README.md
├── app.py
├── analyzer.py
├── llm_analyzer.py
├── rag.py
├── requirements.txt
│
└── knowledge/
```

Make sure these are **not uploaded**:

```text
.env
venv/
vectorstore/
__pycache__/
```

---

# 🔄 Updating the GitHub Repository

Check changes:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Update PhishGuard"
```

Push:

```bash
git push
```

---

# 🤝 Contributing

Contributions and improvements are welcome.

## Basic Contribution Workflow

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd PhishGuard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Create a new branch:

```bash
git checkout -b feature/your-feature
```

Make your changes:

```bash
git add .
```

Commit your changes:

```bash
git commit -m "Add your feature"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Then create a **Pull Request** on GitHub.

---

# 🎯 Project Objective

The goal of **PhishGuard** is to make phishing detection more understandable and accessible by combining:

```text
Rule-Based Security Analysis
            +
       RAG Retrieval
            +
      AI Explanation
            │
            ▼
Explainable Security Assessment
```

Instead of simply returning a risk score, PhishGuard explains:

- 🔍 What makes the content suspicious
- ⚠️ Which indicators were detected
- 🧠 What relevant cybersecurity knowledge applies
- 🛡️ What safe action the user should take

---

# 🏆 Hackathon

| Detail | Information |
|---|---|
| 🚀 Project | **PhishGuard — AI Phishing Message & URL Analyzer** |
| 🏆 Event | **HackDevengers 24-Hour Hackathon** |
| 🔐 Domain | **Cybersecurity + Artificial Intelligence** |
| 🤖 Core Technologies | **Python, LangChain, RAG, FAISS, Hugging Face** |
| 🌐 Live Demo | **[Launch PhishGuard](https://phishgaurd---ai-phishing-message-analyzer-b5aw8qqdualgw83rnvkk.streamlit.app/)** |

---

# 🌐 Live Application

### 🚀 Try PhishGuard

**[👉 Launch the Live PhishGuard Application](https://phishgaurd---ai-phishing-message-analyzer-b5aw8qqdualgw83rnvkk.streamlit.app/)**

The deployed application allows users to analyze suspicious messages and URLs and receive an explainable cybersecurity assessment.

---

# 👩‍💻 Contributors

Developed as a **team project** for the **HackDevengers 24-Hour Hackathon**.

---

# 📄 License

This project is intended for **educational, research, and hackathon purposes**.

---

<p align="center">
  🛡️ <strong>PhishGuard</strong> — Detect. Explain. Protect.
</p>

<p align="center">
  Built with ❤️ using Python, LangChain, RAG, FAISS & Hugging Face
</p>
