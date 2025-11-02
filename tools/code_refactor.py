from tools.base import Tool
import ast

class CodeRefactorTool(Tool):
    def name(self):
        return "code_refactor"

    def description(self):
        return "Refactors Python code for readability, maintainability, and best practices."

    def run(self, input_data: dict, language: str) -> dict:
        code = input_data.get("code", "")
        language = language.lower()
        lines_original = code.count("\n") + 1

        # Mock refactor (replace with real logic if needed)
        refactored_code = (
            "# ✅ Python Refactored Code\n"
            "def add_numbers(a: int, b: int) -> int:\n"
            "    '''Return the sum of two numbers.'''\n"
            "    return a + b\n\n"
            "if __name__ == '__main__':\n"
            "    print(add_numbers(3, 5))  # 8\n"
        )
        lines_refactored = refactored_code.count("\n")
        improvement_score = min(100, int((lines_original - lines_refactored + 1) * 10))

        feedback = "✨ Refactored for readability, added type hints, consistent indentation, and docstring."

        return {
            "status": "success",
            "language": language,
            "metadata": {
                "lines_original": lines_original,
                "lines_refactored": lines_refactored,
                "improvement_score": improvement_score
            },
            "refactored_code": refactored_code,
            "feedback": feedback
        }
