import os
import httpx
from config import MCP_API_KEY

BASE_URL = os.getenv("MCP_SERVER_URL", "http://127.0.0.1:8000")
HEADERS = {"X-API-Key": MCP_API_KEY, "Content-Type": "application/json"}

def call_tool(endpoint: str, payload: dict):
    url = f"{BASE_URL}/run/{endpoint}"
    response = httpx.post(url, json=payload, headers=HEADERS, timeout=30.0)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Example usage
    payload = {"code": "def add(a,b): return a+b", "language": "python"}
    result = call_tool("code_refactor", payload)
    print(result)
