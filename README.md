"# AI_Legal_Assistant" 
# ⚖️ Legal AI Assistant using CrewAI + Ollama

An AI-powered multi-agent Legal Assistant built using CrewAI, Ollama, Streamlit, and Llama3.

This project analyzes legal documents such as contracts, agreements, NDAs, and compliance documents using multiple specialized AI agents working collaboratively.

---

# 🚀 Features

- 📄 Upload legal PDF documents
- 🤖 Multi-Agent AI architecture using CrewAI
- 🧠 Local LLM inference using Ollama
- ⚖️ Legal clause analysis
- ⚠️ Risk assessment
- ✅ Compliance analysis
- 📝 Legal drafting recommendations
- 📋 Executive legal summaries
- 🔒 Fully local and private AI workflow
- 💻 Streamlit web interface

---

# 🏗️ Tech Stack

| Technology | Purpose |
|---|---|
| CrewAI | Multi-agent orchestration |
| Ollama | Local LLM runtime |
| Llama3 | Language model |
| Streamlit | Web UI |
| PyPDF | PDF text extraction |
| Python | Backend logic |

---

# 🧠 Multi-Agent Architecture

The system uses multiple specialized legal AI agents.

## 1. Legal Analysis Agent

### Responsibilities

- Understand legal document structure
- Identify important clauses
- Extract obligations
- Detect termination conditions
- Interpret legal meaning

### Output

- Legal document understanding report
- Clause analysis
- Contract structure overview

---

## 2. Risk Analysis Agent

### Responsibilities

- Identify legal liabilities
- Detect financial exposure
- Analyze indemnity risks
- Detect penalty clauses
- Find dangerous contractual terms

### Output

- Legal risk analysis report
- Liability assessment
- Financial risk overview

---

## 3. Compliance Agent

### Responsibilities

- Identify compliance issues
- Detect governance concerns
- Analyze regulatory risks
- Find policy violations
- Detect compliance gaps

### Output

- Compliance analysis report
- Regulatory concern summary
- Governance assessment

---

## 4. Legal Drafting Agent

### Responsibilities

- Draft legal recommendations
- Suggest improvements
- Recommend corrective actions
- Draft legal observations
- Suggest risk mitigation strategies

### Output

- Professional legal recommendations
- Draft observations
- Suggested corrective actions

---

## 5. Executive Summary Agent

### Responsibilities

- Generate concise summaries
- Highlight key findings
- Summarize major risks
- Present compliance overview
- Create executive-level reports

### Output

- Executive summary report
- Final legal overview
- Key legal findings

---

# 🔄 Workflow

```text
User Uploads PDF
        ↓
Legal Analysis Agent
        ↓
Risk Analysis Agent
        ↓
Compliance Agent
        ↓
Drafting Agent
        ↓
Summary Agent
        ↓
Final Legal Report


Project Structure:
legal-ai-agent/
│
├── app.py
├── ui.py
├── data/
├── requirements.txt
├── README.md
└── venv/

Installation:
1. Clone Repository
git clone <your-repository-url>
cd legal-ai-agent
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install crewai==0.28.8
pip install streamlit
pip install ollama
pip install pypdf
pip install litellm

Install Ollama
Download and install Ollama:
https://ollama.com/download

Pull Llama3 Model
ollama pull llama3
▶️ Run the Application
streamlit run ui.py
🖥️ Application Features

Users can:

Upload legal PDF documents
Analyze contracts
Detect legal risks
Check compliance concerns
Generate executive summaries
View professional legal recommendations
🔒 Privacy Benefits

This project runs fully locally using Ollama.

Benefits:

No OpenAI dependency
No API costs
Complete privacy
Offline legal document analysis

📌 Future Improvements
RAG-based legal search
ChromaDB vector database
Case law retrieval
Legal citation validation
Multi-document analysis
Conversational legal chatbot
Voice-enabled legal assistant
Legal memory system

📜 License
This project is for educational and research purposes.

👨‍💻 Author
Developed by Venkatesh Guttpally using CrewAI + Ollama + Streamlit.