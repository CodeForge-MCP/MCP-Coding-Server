from tools.base import Tool

class CodeDebugTool(Tool):
    def name(self):
        return "code_debug"

    def description(self):
        return "Mocks Python code debugging, detects syntax issues, and provides output preview."

    def run(self, input_data: dict, language: str) -> dict:
        code = input_data.get("code", "")
        language = language.lower()
        feedback = (
            "### Python Debugging Report\n"
            "- ✅ Code executed successfully.\n"
            "- 🧩 No syntax errors found.\n"
            "- 💡 Output preview:\n```\nHello, World!\n```\n"
        )
        return {
            "language": language,
            "feedback": feedback,
            "summary": "Mocked debugging completed successfully (offline mode)."
        }
