from .resume_optimizer import ResumeOptimizer
from .cover_letter import CoverLetter
from .ksc_response import KSCResponse
from .knowledge.loader import KnowledgeLoader
from .utils.helpers import load_experience_db

class AIResumeAgent:
    """
    The main agent class that orchestrates the document generation process.
    """
    def __init__(self):
        """
        Initializes the agent and its components.
        """
        self.knowledge_loader = KnowledgeLoader()
        self.experience_db = load_experience_db()

        self.resume_optimizer = ResumeOptimizer()
        self.cover_letter = CoverLetter()
        self.ksc_response_generator = KSCResponse()

    def _get_relevant_experiences(self, text_to_search: str) -> str:
        """
        A simple search function to find relevant experiences from the database.
        """
        relevant_experiences = []
        search_text_lower = text_to_search.lower()

        for exp in self.experience_db:
            for keyword in exp.get('keywords', []):
                if keyword.lower() in search_text_lower:
                    relevant_experiences.append(exp)
                    break 
        
        if not relevant_experiences:
            return "No specific experiences from the database were found to be relevant."
        
        context_str = "--- Relevant Experiences from Personal Database ---
"
        for exp in relevant_experiences:
            context_str += f"\nSkill/KSC: {exp['skill_or_ksc']}\n"
            context_str += f"Situation: {exp['situation']}\n"
            context_str += f"Task: {exp['task']}\n"
            context_str += f"Action: {exp['action']}\n"
            context_str += f"Result: {exp['result']}\n"
            context_str += "---\n"
            
        return context_str

    def generate_optimized_resume(self, resume: str, job_description: str, ksc: str, user_context: str = "") -> str:
        search_text = job_description + " " + ksc
        relevant_experiences = self._get_relevant_experiences(search_text)
        
        return self.resume_optimizer.optimize(
            resume=resume, 
            job_description=job_description, 
            ksc=ksc,
            user_context=user_context,
            knowledge=self.knowledge_loader.load_knowledge(),
            relevant_experiences=relevant_experiences
        )

    def generate_cover_letter(self, resume: str, job_description: str, ksc: str, user_context: str = "") -> str:
        search_text = job_description + " " + ksc
        relevant_experiences = self._get_relevant_experiences(search_text)
        
        return self.cover_letter.generate(
            resume=resume, 
            job_description=job_description, 
            ksc=ksc,
            user_context=user_context,
            knowledge=self.knowledge_loader.load_knowledge(),
            relevant_experiences=relevant_experiences
        )

    def generate_ksc_responses(self, resume: str, job_description: str, ksc: str, user_context: str = "") -> str:
        search_text = job_description + " " + ksc
        relevant_experiences = self._get_relevant_experiences(search_text)
        
        return self.ksc_response_generator.generate(
            resume=resume, 
            job_description=job_description, 
            ksc=ksc,
            user_context=user_context,
            knowledge=self.knowledge_loader.load_knowledge(),
            relevant_experiences=relevant_experiences
        )