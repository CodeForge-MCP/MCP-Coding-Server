# tools/code_generation.py
from tools.base import Tool
import logging

logger = logging.getLogger("code_generation")

class CodeGenerationTool(Tool):
    def name(self):
        return "code_generation"

    def description(self):
        return "Mock tool that generates sample code for a given prompt and language (offline testing mode)."

    def run(self, input_data: dict, language: str):
        prompt = input_data.get("prompt", "")
        language = language.lower()

        # Mocked output examples per language
        if language == "python":
            code_output = (
                f"# Python code generated for prompt:\n"
                f"# {prompt}\n"
                "def reverse_string(s):\n"
                "    '''Reverse a given string.'''\n"
                "    return s[::-1]\n\n"
                "# Example usage\n"
                "print(reverse_string('hello'))  # 'olleh'\n"
            )

        elif language == "javascript":
            code_output = (
                f"// JavaScript code generated for prompt:\n"
                f"// {prompt}\n"
                "function reverseString(str) {\n"
                "  return str.split('').reverse().join('');\n"
                "}\n\n"
                "console.log(reverseString('hello')); // 'olleh'\n"
            )

        else:
            code_output = (
                f"// Mocked code generation for language: {language}\n"
                f"// Prompt: {prompt}\n"
                "// This is placeholder output.\n"
            )

        logger.info(f"[MOCK] Code generated for language={language}, prompt={prompt}")

        return {
            
            "language": language,
            "prompt": prompt,
            "code": code_output
        }
