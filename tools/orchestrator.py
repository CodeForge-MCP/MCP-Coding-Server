from tools.code_review import CodeReviewTool
from tools.code_refactor import CodeRefactorTool
from tools.code_debug import CodeDebugTool

class ToolOrchestrator:
    def __init__(self):
        self.review_tool = CodeReviewTool()
        self.refactor_tool = CodeRefactorTool()
        self.debug_tool = CodeDebugTool()

    def run_full_pipeline(self, input_data: dict, language: str):
        # Step 1: Review
        review_result = self.review_tool.run(input_data, language)

        # Step 2: Refactor
        refactor_result = self.refactor_tool.run(input_data, language)

        # Step 3: Debug
        debug_result = self.debug_tool.run(input_data, language)

        # Compute improvement score dynamically
        improvement_score = self.calculate_score(review_result, refactor_result)

        # Return combined results
        return {
            "status": "success",
            "review": review_result,
            "refactor": {**refactor_result, "metadata": {**refactor_result.get("metadata", {}), "improvement_score": improvement_score}},
            "debug": debug_result
        }

    def calculate_score(self, review_result, refactor_result):
        # Basic scoring: start from 100, deduct for issues
        score = 100
        issues = review_result.get("agent_notes", [])
        if issues:
            deduction = min(len(issues) * 5, 100)
            score -= deduction
        return max(score, 0)
