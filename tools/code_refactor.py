# tools/code_refactor.py
from tools.base import Tool
import logging

logger = logging.getLogger("code_refactor")

class CodeRefactorTool(Tool):
    def name(self):
        return "code_refactor"

    def description(self):
        return "Mock tool that refactors code and returns a cleaner version (offline testing mode)."

    def run(self, input_data: dict, language: str):
        code = input_data.get("code", "")
        language = language.lower()

        # Mock refactoring behavior per language
        if language == "python":
            refactored_code = (
                "# Python refactored version:\n"
                "def add_numbers(a: int, b: int) -> int:\n"
                "    '''Return the sum of two numbers.'''\n"
                "    return a + b\n\n"
                "# Example usage\n"
                "print(add_numbers(3, 5))  # 8\n"
            )
            feedback = "Code refactored with improved readability, typing hints, and spacing."

        elif language == "javascript":
            refactored_code = (
                "// JavaScript refactored version:\n"
                "function addNumbers(a, b) {\n"
                "  // Return the sum of two numbers\n"
                "  return a + b;\n"
                "}\n\n"
                "console.log(addNumbers(3, 5)); // 8\n"
            )
            feedback = "Code refactored for consistent indentation and clear comments."

        else:
            refactored_code = (
                f"// Mock refactor for {language} code\n"
                "// Original structure preserved; improvements suggested.\n"
            )
            feedback = f"Basic mock refactor for {language} completed."

        logger.info(f"[MOCK] Code refactored for language={language}")

        return {
            "language": language,
            "refactored_code": refactored_code,
            "feedback": feedback
        }


# --------------------------
# Optional local test block
# --------------------------
if __name__ == "__main__":
    import json

    tool = CodeRefactorTool()

    mock_inputs = [
        {"code": "def add(a,b):return a+b", "language": "python"},
        {"code": "function add(a,b){return a+b;}", "language": "javascript"},
    ]

    for inp in mock_inputs:
        result = tool.run(inp, inp["language"])
        print(f"\nInput:\n{json.dumps(inp, indent=2)}")
        print(f"Mock Output:\n{json.dumps(result, indent=2)}")
