from tools.base import Tool
import logging

logger = logging.getLogger("code_review")

class CodeReviewTool(Tool):
    def name(self):
        return "code_review"

    def description(self):
        return "Mock tool that reviews code and provides example feedback for offline testing."

    def run(self, input_data: dict, language: str):
        code = input_data.get("code", "")
        language = language.lower()

        # Mocked feedback examples per language
        if language == "python":
            feedback = (
                "### Python Code Review Feedback\n"
                "- ✅ Code syntax looks correct.\n"
                "- ⚙️ Consider adding docstrings for better documentation.\n"
                "- 🧩 Variable naming is clear, no obvious style violations.\n"
                "- 💡 Tip: Ensure consistent indentation (4 spaces recommended).\n"
            )

        elif language == "javascript":
            feedback = (
                "### JavaScript Code Review Feedback\n"
                "- ✅ Syntax and structure look fine.\n"
                "- ⚙️ Consider using `const` and `let` instead of `var`.\n"
                "- 🧩 Check for proper semicolon usage and consistent spacing.\n"
                "- 💡 You might wrap logic in functions for reusability.\n"
            )

        else:
            feedback = (
                f"### Code Review for {language.title()}\n"
                "- ⚙️ Mocked feedback for offline mode.\n"
                "- 🧩 No syntax analysis available.\n"
                "- 💡 Ensure consistent formatting and naming conventions.\n"
            )

        logger.info(f"[MOCK] Code reviewed for language={language}")

        return {
            "language": language,
            "feedback": feedback,
            "summary": "Mocked code review completed successfully (offline mode)."
        }
if __name__ == "__main__":
    import json

    tool = CodeReviewTool()

    mock_inputs = [
        {"code": "def add(a, b): return a + b", "language": "python"},
        {"code": "function add(a, b) { return a + b; }", "language": "javascript"},
        {"code": "<html><body>Hello</body></html>", "language": "html"},
    ]

    for inp in mock_inputs:
        result = tool.run(inp, inp["language"])
        print(f"\nInput:\n{json.dumps(inp, indent=2)}")
        print(f"Mock Output:\n{json.dumps(result, indent=2)}")