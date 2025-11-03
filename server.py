from fastapi import FastAPI, Request, Depends, Header, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pathlib import Path
 
# === Config import ===
from config import MCP_API_KEY
 
# === Auth ===
def require_auth(x_api_key: str = Header(...)):
    if x_api_key != MCP_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
 
# === App setup ===
app = FastAPI(title="MCP Coding Server", version="1.1")
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can restrict later to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# === Template setup ===
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
 
@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("ui.html", {"request": request})
 
# === Tool imports ===
from tools.code_review import CodeReviewTool
from tools.code_refactor import CodeRefactorTool
from tools.code_debug import CodeDebugTool
from tools.code_generation import CodeGenerationTool
from tools.orchestrator import ToolOrchestrator
 
# === Schemas ===
from schemas import CodeReviewInput, CodeRefactorInput, CodeDebugInput, CodeGenerationInput
 
# === Tool registry ===
tools_registry = {
    "code_review": CodeReviewTool(),
    "code_refactor": CodeRefactorTool(),
    "code_debug": CodeDebugTool(),
    "code_generation": CodeGenerationTool(),
}
 
# === Orchestrator instance ===
orchestrator = ToolOrchestrator()
 
# === Tool routes ===
@app.post("/run/code_review")
async def run_code_review(input: CodeReviewInput, auth=Depends(require_auth)):
    tool = tools_registry["code_review"]
    return tool.run(input.dict(), input.language)
 
@app.post("/run/code_refactor")
async def run_code_refactor(input: CodeRefactorInput, auth=Depends(require_auth)):
    tool = tools_registry["code_refactor"]
    return tool.run(input.dict(), input.language)
 
@app.post("/run/code_debug")
async def run_code_debug(input: CodeDebugInput, auth=Depends(require_auth)):
    tool = tools_registry["code_debug"]
    return tool.run(input.dict(), input.language)
 
@app.post("/run/code_generation")
async def run_code_generation(input: CodeGenerationInput, auth=Depends(require_auth)):
    tool = tools_registry["code_generation"]
    return tool.run(input.dict(), input.language)
 
@app.post("/run/full_pipeline")
async def run_full_pipeline(input: CodeReviewInput, auth=Depends(require_auth)):
    return orchestrator.run_full_pipeline(input.dict(), input.language)
 
@app.get("/tools")
async def list_tools(auth=Depends(require_auth)):
    return [{"name": t.name(), "description": t.description()} for t in tools_registry.values()]