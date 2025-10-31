# client.py
import os
import httpx

BASE_URL = os.getenv("MCP_SERVER_URL", "http://127.0.0.1:8000")
API_KEY = os.getenv("MCP_API_KEY", "mysecureapikey")
HEADERS = {"X-API-Key": API_KEY, "Content-Type": "application/json"}

def list_tools():
    try:
        r = httpx.get(f"{BASE_URL}/tools", headers=HEADERS, timeout=10.0)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error listing tools:", e)
        return None

def run_tool(tool_name, payload):
    try:
        r = httpx.post(f"{BASE_URL}/run/{tool_name}", headers=HEADERS, json=payload, timeout=60.0)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error running tool:", e)
        return None

def create_prompt(name, tool, language, template):
    try:
        r = httpx.post(f"{BASE_URL}/prompts", headers=HEADERS, json={"name": name, "tool": tool, "language": language, "template": template}, timeout=10.0)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error creating prompt:", e)
        return None

def list_prompts():
    try:
        r = httpx.get(f"{BASE_URL}/prompts", headers=HEADERS, timeout=10.0)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error listing prompts:", e)
        return None

if __name__ == "__main__":
    print("Tools:", list_tools())
