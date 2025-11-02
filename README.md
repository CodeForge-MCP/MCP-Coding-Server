# CodeForge MCP — AI Coding Server (FastAPI + MCP Protocol)

* CodeForge MCP is a modular AI coding server built with FastAPI and following the Model Context Protocol (MCP) standard.
 It enables AI agents and developers to securely run code review, refactoring, and debugging operations via REST APIs and an interactive browser UI.
--- 

🌍 Live Deployment
🔗 Live URL: [(https://mcp-coding-server.onrender.com/)](https://mcp-coding-server.onrender.com/)


## Features

- **⚙️FastAPI backend** — lightweight, async, and scalable

- **🧰 Tool modules** — code review, refactor, and debug, each as an independent module
- **🔒 API key protection** — secure every request with header-based authentication
- **💻 Web UI (Jinja2)** — interact with tools visually in your browser
- **🔁 Full pipeline mode** — run all tools together for a unified result
- **📊 Pylint-powered static analysis** — catch code issues and style violations automatically
  
## Project Structure
MCP Coding Server/

├── server.py                  # Main FastAPI app (entry point)

├── client.py                  # Client to test APIs locally

├── tools/

│   ├── code_review.py         # Runs static analysis (Pylint)

│   ├── code_refactor.py       # Handles refactoring logic

│   ├── code_debug.py          # Mock debugging logic

│   ├── orchestrator.py        # Combines tools for full pipeline

├── schemas/

│   └── __init__.py            # Pydantic models for validation

├── templates/

│   └── ui.html                # Web UI (Jinja2 + JS fetch API)

├── config.py                  # Central config (loads .env vars)

├── .env                       # Environment variables (local only)

├── requirements.txt           # Python dependencies

└── README.md                 

## Installation (Local Setup)
- **1️⃣ Clone the Repository**
git clone https://github.com/yourusername/mcp-coding-server.git
cd mcp-coding-server

- **2️⃣ Create Virtual Environment**
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
  
- **3️⃣ Install Dependencies**
pip install -r requirements.txt
  
- **4️⃣ Add Environment Variables**
## Create a .env file:

⚠️ Never commit .env to GitHub — keep secrets private!

## Run the Server
uvicorn server:app --reload

Then open http://127.0.0.1:8000

## Authentication
All API requests require the correct API key header:

If the key is invalid, you’ll receive:

401 Unauthorized

## Requirements
- fastapi
- uvicorn
- python-dotenv
- pydantic
- httpx
- pylint
- jinja2
## Development Tools
- Tool	Description
- pylint	Code analysis and linting
- flake8	Style checks
 

