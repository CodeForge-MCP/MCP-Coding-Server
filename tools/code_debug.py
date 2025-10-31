# tools/code_debug.py
from tools.base import Tool
import logging

logger = logging.getLogger("code_debug")

class CodeDebugTool(Tool):
    def name(self):
        return "code_debug"

    def description(self):
        return "Mock tool that simulates debugging output for offline testing."

    def run(self, input_data: dict, language: str):
        code = input_data.get("code", "")
        language = language.lower()

        # Mocked debugging output per language
        if language == "python":
            feedback = (
                "### Python Debugging Report\n"
                "- ✅ Code executed successfully.\n"
                "- 🧩 No syntax errors found.\n"
                "- 💡 Output preview:\n"
                "```\nHello, World!\n```\n"
            )

        elif language == "javascript":
            feedback = (
                "### JavaScript Debugging Report\n"
                "- ✅ Script ran without exceptions.\n"
                "- 🧩 Console output:\n"
                "```\nHello, World!\n```\n"
            )

        else:
            feedback = (
                f"### Debugging Report for {language.title()}\n"
                "- ⚙️ Execution simulated.\n"
                "- 🧩 No real runtime executed (mock mode).\n"
            )

        logger.info(f"[MOCK] Debugging simulated for language={language}")

        return {
            "language": language,
            "feedback": feedback,
            "summary": "Mocked debugging completed successfully (offline mode)."
        }


# --------------------------
# Optional local test block
# --------------------------
if __name__ == "__main__":
    import json

    tool = CodeDebugTool()

    mock_inputs = [
        {"code": "print('Hello, World!')", "language": "python"},
        {"code": "console.log('Hello, World!');", "language": "javascript"},
    ]

    for inp in mock_inputs:
        result = tool.run(inp, inp["language"])
        print(f"\nInput:\n{json.dumps(inp, indent=2)}")
        print(f"Mock Output:\n{json.dumps(result, indent=2)}")
