# SilentRisk-AI-Dev-Risk-Agent
SilenSilentRisk AI – Dev Risk Agent
SilentRisk AI is an AI-powered developer risk detection agent built with Gemini and Google Cloud Agent Builder.
The system analyzes incoming GitLab commits, detects hidden security and logic risks, and automatically generates actionable GitLab issues with severity classification and fix suggestions.
🚀 Features
Detects risky code changes
AI-powered semantic risk analysis
Severity classification (Low, Medium, High, Critical)
Automatic GitLab issue generation
Suggested fix recommendations
MCP-based workflow design
Simple live demo prototype
🧠 How It Works
Plain text
GitLab Commit
      ↓
MCP Server
      ↓
SilentRisk AI (Gemini Agent)
      ↓
Risk Analysis
      ↓
Automatic GitLab Issue Creation
⚙️ Tech Stack
Python
Flask
Gemini API
Google Cloud Agent Builder
GitLab MCP Architecture
HTML/CSS
📂 Project Structure
Plain text
silentrisk-ai/
│
├── main.py
├── sample_commit.json
├── templates/
│   └── index.html
└── README.md
▶️ Running the Project
1. Clone Repository
Bash
git clone https://github.com/yourusername/silentrisk-ai.git
2. Install Dependencies
Bash
pip install flask
3. Run Application
Bash
python main.py
📸 Demo Workflow
Incoming GitLab commit detected
SilentRisk AI analyzes changes
High-risk vulnerabilities identified
Automatic issue generated with suggested fixes
🔥 Example Detection
Incoming Commit
JSON
{
  "file": "auth/login.py",
  "change": "Removed password validation"
}
AI Output
Plain text
HIGH RISK:
Authentication bypass vulnerability detected.
📌 Future Improvements
Real GitLab API integration
Elastic/Dynatrace support
Advanced AI threat scoring
Dashboard analytics
Human approval workflows
👩‍💻 Built For
Google Cloud Rapid Agent Hackathon 2026
Built using Gemini + Google Cloud Agent Builder.tRisk AI is an AI-powered developer risk detection agent built with Gemini and Google Cloud Agent Builder. The system analyzes incoming GitLab commits, detects hidden security and logic risks, and automatically generates actionable GitLab issues with severity classification and fix suggestions.
