import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from .utils.config import get_settings
from .utils.llm import get_model
from .Prompt_builder import PromptBuilder
from .schemas.models import CoverLetterOutput

class CoverLetter:
    def __init__(self):
        self.settings = get_settings()
        self.model = get_model()
        self.prompts = PromptBuilder()

        template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_dir))

    def generate(self, resume: str, job_description: str, ksc: str, user_context: str = "", knowledge: str = "", relevant_experiences: str = ""):
        prompt_template = self.prompts.get_prompt("cover-letter")
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
                generation_config={"response_mime_type": "application/json", "response_schema": CoverLetterOutput}
            )
            ai_data = CoverLetterOutput.model_validate_json(response.text)

        except Exception as e:
            print(f"Error generating structured output: {e}")
            return f"AI Structured Output Error. Details: {e}"

        template = self.jinja_env.get_template("cover_letter_template.md")
        
        template_data = {
            "date": datetime.now().strftime("%d %B %Y"),
            "full_name": "Mx. Nishant Jonas Dougall",
            "address": "Unit 2 418 High Street, Northcote VICTORIA 3070, Australia",
            "phone": "+61412202666",
            "email": "nishant.dougall@example.com",
            "job_title": ai_data.job_title,
            "company_name": ai_data.company_name,
            "hiring_manager": ai_data.hiring_manager,
            "ai_generated_body": ai_data.ai_generated_body
        }

        formatted_cover_letter = template.render(template_data)
        return formatted_cover_letter