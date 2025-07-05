import os
import yaml
import functools

class KnowledgeLoader:
    """
    A dedicated class for loading and caching knowledge files from the
    'knowledge/sources' directory.
    """
    def __init__(self):
        # Defines the path to the knowledge source files relative to this file's location
        self.knowledge_path = os.path.join(
            os.path.dirname(__file__), 'sources'
        )

    @functools.lru_cache(maxsize=None)
    def load_knowledge(self) -> str:
        """
        Loads all .yaml files from the knowledge/sources directory,
        concatenates their content, and returns it as a single string.
        """
        all_knowledge = ""
        
        if not os.path.isdir(self.knowledge_path):
            print(f"Warning: Knowledge directory not found at {self.knowledge_path}")