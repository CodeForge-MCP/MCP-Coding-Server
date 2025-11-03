# schemas.py
from pydantic import BaseModel
 
class CodeReviewInput(BaseModel):
    code: str
    language: str
 
class CodeGenerationInput(BaseModel):
    code: str
    language: str
 
class CodeRefactorInput(BaseModel):
    code: str
    language: str
 
class CodeDebugInput(BaseModel):
    code: str
    language: str