from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("sample_commit.json", "r", encoding="utf-8") as file:
        commit = json.load(file)

    risk = {
        "level": "HIGH",
        "problem": "Authentication bypass vulnerability detected.",
        "fix": "Restore password verification."
    }

    issue = {
        "title": "High Risk Change Detected",
        "severity": "High",
        "status": "Issue Created Automatically"
    }

    return render_template(
        "index.html",
        commit=commit,
        risk=risk,
        issue=issue
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=False)
