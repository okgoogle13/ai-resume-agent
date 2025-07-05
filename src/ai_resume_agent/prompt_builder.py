import os
import yaml
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class PromptBuilder:
    """
    Handles loading and managing prompts from YAML files.
    """

    def __init__(self):
        self.prompts_path = os.path.join(
            os.path.dirname(__file__), 'prompts', 'Prompts.yaml'
        )
        self._prompts = None

    def _load_prompts(self) -> Dict:
        """Load prompts from YAML file."""
        if self._prompts is None:
            try:
                with open(self.prompts_path, 'r', encoding='utf-8') as f:
                    self._prompts = yaml.safe_load(f)
                logger.info(f"Successfully loaded prompts from {self.prompts_path}")
            except FileNotFoundError:
                logger.error(f"Prompts file not found at {self.prompts_path}")
                raise FileNotFoundError(f"Prompts file not found at {self.prompts_path}")
            except yaml.YAMLError as e:
                logger.error(f"Error parsing YAML file: {e}")
                raise ValueError(f"Error parsing YAML file: {e}")
        return self._prompts

    def get_prompt(self, prompt_key: str) -> str:
        """
        Get a specific prompt by key.

        Args:
            prompt_key: The key of the prompt to retrieve

        Returns:
            The prompt template string

        Raises:
            KeyError: If the prompt key is not found
        """
        prompts = self._load_prompts()
        if prompt_key not in prompts:
            available_keys = list(prompts.keys())
            raise KeyError(f"Prompt '{prompt_key}' not found. Available prompts: {available_keys}")

        return prompts[prompt_key]

    def get_all_prompts(self) -> Dict:
        """Get all available prompts."""
        return self._load_prompts()

    def list_available_prompts(self) -> list:
        """List all available prompt keys."""
        prompts = self._load_prompts()
        return list(prompts.keys())
