from typing import Optional, Dict, Any
from pydantic import BaseModel

class CodeGenerationInput(BaseModel):
    language: Optional[str] = "python"
    prompt: Optional[str] = None

class CodeReviewInput(BaseModel):
    code: str
    language: Optional[str] = "python"
    prompt: Optional[str] = None

class CodeRefactorInput(BaseModel):
    code: str
    instructions: Optional[str] = None
    language: Optional[str] = "python"

class CodeDebugInput(BaseModel):
    code: str
    language: Optional[str] = "python"

class ToolInput(BaseModel):
    tool_name: str
    input_data: Dict[str, Any]

