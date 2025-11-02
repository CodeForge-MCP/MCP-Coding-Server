import ast
import subprocess
import tempfile
import re
from tools.base import Tool

class CodeReviewTool(Tool):
    def name(self):
        return "code_review"

    def description(self):
        return "Analyzes Python code for structure, functions, security, and basic code issues."

    def run(self, input_data: dict, language: str) -> dict:
        code = input_data.get("code", "")
        mode = input_data.get("mode", "default")

        if language.lower() != "python":
            return {
                "summary": f"❌ Code review for '{language}' not supported.",
                "functions_found": [],
                "suggestions": [],
                "agent_notes": []
            }

        try:
            tree = ast.parse(code)
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            suggestions = []

            if not functions:
                suggestions.append("⚠️ No functions defined.")
            if "main" not in functions:
                suggestions.append("ℹ️ Consider adding a main() entry point.")
            if len(functions) > 5:
                suggestions.append("🔍 Code has many functions — consider splitting into modules.")

            pylint_raw = self.run_pylint(code)
            agent_notes = self.parse_pylint_feedback(pylint_raw)

            security_notes = self.run_security_audit(code, tree)
            agent_notes.extend(security_notes)

            return {
                "summary": "⚠️ Code parsed successfully, but potential security issues were found." if security_notes else "✅ Code parsed successfully.",
                "functions_found": functions,
                "suggestions": suggestions or ["👍 No major issues found."],
                "agent_notes": sorted(set(agent_notes))
            }

        except SyntaxError as e:
            return {
                "summary": "❌ Syntax error in code.",
                "error": str(e),
                "functions_found": [],
                "suggestions": ["🛠️ Fix the syntax error before reviewing."],
                "agent_notes": []
            }

    def run_pylint(self, code: str) -> str:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name

        result = subprocess.run(
            ["pylint", temp_path, "--disable=all", "--enable=E,W,C,R,F"],
            capture_output=True,
            text=True
        )
        return result.stdout

    def parse_pylint_feedback(self, feedback: str) -> list:
        lines = feedback.strip().splitlines()
        notes = set()
        for line in lines:
            match = re.search(r": ([CRWEF]\d{4}): (.+)", line)
            if match:
                code = match.group(1)
                message = match.group(2).strip()
                if "missing-module-docstring" in message:
                    notes.add("📘 Add a module-level docstring to describe the file's purpose.")
                elif "missing-function-docstring" in message:
                    notes.add("📝 Add docstrings to your functions to explain their behavior.")
                else:
                    notes.add(f"🔍 {message} ({code})")

        score_match = re.search(r"rated at ([\d\.]+)/10", feedback)
        if score_match:
            score = float(score_match.group(1))
            if score < 10.0:
                notes.add(f"📊 Code scored {score}/10 on pylint — consider addressing the issues above.")
            else:
                notes.add("✅ Code scored 10/10 on pylint — no issues found.")

        return sorted(notes)

    def run_security_audit(self, code: str, tree: ast.AST) -> list:
        findings = []
        risky_keywords = ["eval", "exec", "pickle"]
        for keyword in risky_keywords:
            if keyword in code:
                findings.append(f"🛑 Dangerous function call `{keyword}` detected — may lead to code execution risk.")

        secret_keywords = ["password", "api_key", "token", "secret"]
        for line in code.splitlines():
            if any(k in line.lower() for k in secret_keywords) and re.search(r"=\s*[\"'].*[\"']", line):
                findings.append("🔐 Hardcoded secrets detected — use environment variables or config files instead.")

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.args.args:
                body_text = ast.get_source_segment(code, node) or ""
                if not any(kw in body_text for kw in ["if", "try", "assert"]):
                    findings.append(f"🧪 Function `{node.name}` takes input but lacks validation logic.")

        return findings
