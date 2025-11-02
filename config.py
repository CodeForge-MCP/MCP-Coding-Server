# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Centralized API key
MCP_API_KEY = os.getenv("MCP_API_KEY", "mysecureapikey")  # fallback for local testing
