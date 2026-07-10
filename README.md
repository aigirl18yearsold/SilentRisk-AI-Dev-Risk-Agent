# SilentRisk AI – Dev Risk Agent

## Overview

SilentRisk AI is an AI-powered developer risk detection agent designed to help development teams identify security vulnerabilities and risky code changes before deployment. Built with Google Gemini and Google Cloud Agent Builder, the system analyzes GitLab commits, detects hidden security and logic issues, classifies their severity, and automatically generates GitLab issues with AI-powered fix recommendations.

By automating early risk detection, SilentRisk AI helps developers improve software quality, reduce manual code review effort, and strengthen application security.

---

## Features

- AI-powered semantic analysis of GitLab commits
- Detects security and logic vulnerabilities
- Severity classification (Low, Medium, High, Critical)
- Automatic GitLab issue generation
- AI-generated fix recommendations
- Simple web interface for testing
- MCP-based workflow architecture

---

## How It Works

1. A GitLab commit is submitted for analysis.
2. Gemini AI examines the code changes.
3. Security and logic risks are detected.
4. Each issue is assigned a severity level.
5. GitLab issues are automatically generated.
6. AI provides actionable recommendations to resolve the detected risks.

---

## Tech Stack

- Python
- Flask
- Google Gemini API
- Google Cloud Agent Builder
- GitLab
- HTML
- CSS

---

## Project Structure

```
main.py
sample_commit.json
templates/
└── index.html
README.md
```

---

## Installation

Install the required dependency:

```bash
pip install flask
```

Run the application:

```bash
python main.py
```

Open the application in your browser to analyze sample GitLab commits.

---

## Example

### Sample Commit


Removed password validation from login.py


### AI Analysis

**Severity:** High

**Detected Risk:** Authentication bypass vulnerability

**Recommendation:** Restore password validation, verify authentication logic, and perform additional security testing before deployment.

## Startup Vision

SilentRisk AI aims to become an intelligent DevSecOps platform that enables development teams to identify risky code changes before deployment using AI-powered analysis, automated issue generation, and actionable security recommendations.

## Future Improvements

- Real-time GitLab API integration
- Advanced AI threat scoring
- Interactive analytics dashboard
- Human approval workflow
- Multi-repository support
- Cloud deployment

## Built For

This project was developed as a prototype for the **InnovatorsX: Startup Sprint 2026**, showcasing how AI can help development teams detect software risks early, improve code quality, and automate security-focused workflows.

## Author

Developed by **Homyra Akther shaila** as an AI-powered prototype for intelligent developer risk detection using Google Gemini and Google Cloud technologies.

---

## License

This project is intended for educational, research, and hackathon purposes.
