# tools/code_generation.py
from tools.base import Tool
import logging
 
logger = logging.getLogger("code_generation")
 
class CodeGenerationTool(Tool):
    def name(self):
        return "code_generation"
 
    def description(self):
        return "Generates mock code for a given prompt and language."
 
    def run(self, input_data: dict, language: str):
        prompt = input_data.get("code", "")
        language = language.lower()
 
        if language == "python":
            code_output = (
                f"# Generated Python code for prompt:\n"
                f"# {prompt}\n\n"
                "def reverse_string(s):\n"
                "    '''Reverse a given string.'''\n"
                "    return s[::-1]\n\n"
                "print(reverse_string('hello'))  # 'olleh'\n"
            )
        elif language == "javascript":
            code_output = (
                f"// Generated JavaScript code for prompt:\n"
                f"// {prompt}\n\n"
                "function reverseString(str) {\n"
                "  return str.split('').reverse().join('');\n"
                "}\n\n"
                "console.log(reverseString('hello')); // 'olleh'\n"
            )
        else:
            code_output = (
                f"// Generated mock code for {language}\n"
                f"// Prompt: {prompt}\n"
                "// This is placeholder output.\n"
            )
 
        logger.info(f"Code generated for {language}")
        return {"language": language, "prompt": prompt, "code": code_output}