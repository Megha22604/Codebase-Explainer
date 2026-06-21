# 🧭 Codebase Explainer

> An AI-powered tool that reads any GitHub repository and automatically generates a complete onboarding guide for new developers.

---

## 💡 What It Does

Ever cloned a new project and had no idea where to start?

This tool solves that. Give it any GitHub repo URL — it reads all the code, sends it to Google Gemini AI, and generates a structured onboarding guide explaining exactly what the project does, how it's organized, and where to start reading.

**Input:** A GitHub repo URL  
**Output:** A beautiful onboarding guide — displayed in the terminal AND saved as a `.md` file

---

## ✨ Features

- 📥 Fetches all files from any public GitHub repository
- 🧠 Sends code to Google Gemini AI for intelligent analysis
- 📋 Generates a structured report with 5 sections:
  - Project Summary
  - Tech Stack
  - File Breakdown
  - How to Start
  - Gotchas & Non-obvious things
- 🎨 Displays output beautifully in the terminal using Rich
- 💾 Saves the report as a shareable `.md` file
- ⚡ Handles errors gracefully — skips binary files, handles network issues

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Google Gemini API | AI analysis of codebase |
| PyGithub | Fetch files from GitHub |
| python-dotenv | Manage API keys securely |
| Rich | Beautiful terminal output |

---

## 📁 Project Structure

```
codebase-explainer/
├── day1.py        # Fetch file names from GitHub repo
├── day2.py        # Read actual file contents
├── day3.py        # Send contents to Gemini AI
├── day4.py        # Parse and display response beautifully
├── day5.py        # Save report as .md file (final version)
├── .gitignore     # Keeps API keys safe
└── output/        # Generated reports saved here
```

> **Note:** Each day builds on the previous one. `day5.py` is the complete final version.

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/codebase-explainer.git
cd codebase-explainer
```

### 2. Install dependencies
```bash
pip install PyGithub python-dotenv google-genai rich
```

### 3. Get your API keys

**GitHub Token:**
- Go to GitHub → Settings → Developer Settings → Personal Access Tokens
- Generate a new token with `repo` scope
- Copy the token

**Gemini API Key:**
- Go to [aistudio.google.com](https://aistudio.google.com)
- Sign in with Google → Get API Key
- Copy the key

### 4. Create a `.env` file
```
GITHUB_TOKEN=your_github_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the tool
```bash
python day5.py
```

---

## 🚀 Usage

```bash
python day5.py

🔗 Enter GitHub repo URL: https://github.com/pallets/flask
```

The tool will:
1. Fetch all files from the repo
2. Send them to Gemini AI
3. Display the analysis in beautiful terminal panels
4. Save a `.md` report in the `output/` folder

---

## 📄 Sample Output

```
═══════════════════════════════════════════════════════
  🧭 CODEBASE ONBOARDING GUIDE
  https://github.com/pallets/flask
═══════════════════════════════════════════════════════

╭─ 📌 PROJECT SUMMARY ──────────────────────────────╮
│  Flask is a lightweight web framework for Python.  │
│  It helps developers build web apps quickly        │
│  without unnecessary boilerplate code.             │
╰────────────────────────────────────────────────────╯

╭─ 🧰 TECH STACK ───────────────────────────────────╮
│  - Python                                          │
│  - Jinja2 (templating)                             │
│  - Werkzeug (HTTP handling)                        │
╰────────────────────────────────────────────────────╯

╭─ 🚀 HOW TO START ─────────────────────────────────╮
│  1. Read app.py first                              │
│  2. Then explore routes.py                         │
│  3. Check requirements.txt for dependencies        │
╰────────────────────────────────────────────────────╯
```

A `.md` file is also saved to `output/` automatically.

---

## 🔒 Security

- API keys are stored in `.env` and never committed to GitHub
- `.env` is listed in `.gitignore`
- Never hardcode API keys directly in your code

---

## 🌱 What I Learned Building This

This was my first real Python project beyond tutorials. Built in 5 days, I learned:

- Working with real APIs (GitHub API + Google Gemini API)
- Recursion for traversing nested folder structures
- Error handling with try/except
- Prompt engineering for better AI responses
- String parsing to extract structured data
- Building beautiful terminal UIs with Rich

---

## 🔭 Future Improvements

- [ ] Add a Streamlit web UI
- [ ] Support private GitHub repositories
- [ ] Export report as PDF
- [ ] Add support for GitLab and Bitbucket
- [ ] Auto-generate a project diagram

---

## 👩‍💻 Author

**Megha Jitendra Patil**  
Fresher | Python & AI Enthusiast  


---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
