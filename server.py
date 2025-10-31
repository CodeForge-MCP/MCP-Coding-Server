# server.py
from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
load_dotenv()

from tools.code_generation import CodeGenerationTool
from tools.code_review import CodeReviewTool
from tools.code_refactor import CodeRefactorTool
from tools.code_debug import CodeDebugTool
from tools.prompt_manager import manager as prompt_manager
from schemas import CodeGenerationInput, CodeReviewInput, CodeRefactorInput, CodeDebugInput

API_KEY = "mysecureapikey"
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Template and static setup
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
if (BASE_DIR / "static").exists():
    app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Tool registry
tools_registry = {
    "code_generation": CodeGenerationTool(),
    "code_review": CodeReviewTool(),
    "code_refactor": CodeRefactorTool(),
    "code_debug": CodeDebugTool(),
}

# -------------------------
# UI Route
# -------------------------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    try:
        return templates.TemplateResponse("ui.html", {"request": request})
    except Exception as e:
        print("❌ Template load error:", e)
        return HTMLResponse("<h1>MCP Coding Server</h1><p>UI template not found.</p>")

# -------------------------
# Tool Execution Route
# -------------------------
@app.post("/run/{tool_name}")
async def run_tool(tool_name: str, request: Request, x_api_key: str = Header(None)) -> Dict[str, Any]:
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    data = await request.json()
    tool = tools_registry.get(tool_name)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    if tool_name == "code_generation":
        parsed = CodeGenerationInput(**data)
        return tool.run({"prompt": parsed.prompt}, parsed.language)
    elif tool_name == "code_review":
        parsed = CodeReviewInput(**data)
        return tool.run({"code": parsed.code}, parsed.language)
    elif tool_name == "code_refactor":
        parsed = CodeRefactorInput(**data)
        return tool.run({"code": parsed.code}, parsed.language)
    elif tool_name == "code_debug":
        parsed = CodeDebugInput(**data)
        return tool.run({"code": parsed.code}, parsed.language)
    else:
        raise HTTPException(status_code=400, detail="Unsupported tool")

# -------------------------
# List Available Tools
# -------------------------
@app.get("/tools")
async def list_tools_endpoint(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return [{"name": t.name(), "description": t.description()} for t in tools_registry.values()]

# -------------------------
# Prompt Management Endpoints
# -------------------------
@app.post("/prompts")
async def create_prompt_endpoint(request: Request, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    data = await request.json()
    prompt = prompt_manager.create_prompt(
        name=data["name"],
        tool=data["tool"],
        language=data.get("language", "python"),
        template=data["template"]
    )
    return prompt

@app.get("/prompts")
async def list_prompts_endpoint(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return prompt_manager.list_prompts()
