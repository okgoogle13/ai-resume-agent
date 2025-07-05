import os
from jinja2 import Environment, FileSystemLoader

from .utils.config import get_settings
from .utils.llm import get_model
from .Prompt_builder import PromptBuilder
from .schemas.models import OptimizedResumeOutput

class ResumeOptimizer:
    def __init__(self):
        self.settings = get_settings()
        self.model = get_model()
        self.prompts = PromptBuilder()

        template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_dir))

    def optimize(self, resume: str, job_description: str, ksc: str, user_context: str = "", knowledge: str = "", relevant_experiences: str = ""):
        prompt_template = self.prompts.get_prompt("resume-optimizer")
        prompt = prompt_template.format(
            resume=resume,
            job_description=job_description,
            ksc=ksc,
            user_context=user_context,
            knowledge=knowledge,
            relevant_experiences=relevant_experiences
        )
        
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json", "response_schema": OptimizedResumeOutput}
            )
            ai_data = OptimizedResumeOutput.model_validate_json(response.text)
        except Exception as e:
            print(f"Error generating structured resume output: {e}")
            return f"AI Structured Output Error. Details: {e}"

        template = self.jinja_env.get_template("resume_template.md")
        
        template_data = {
            "full_name": "Mx. Nishant Jonas Dougall",
            "address": "Unit 2 418 High Street, Northcote VICTORIA 3070, Australia",
            "phone": "+61412202666",
            "email": "nishant.dougall@example.com",
            "ai_optimized_resume": ai_data
        }

        formatted_resume = template.render(template_data)
        return formatted_resume