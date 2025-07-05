import google.generativeai as genai
from .config import get_settings
import logging
import time
from typing import Optional
import functools

logger = logging.getLogger(__name__)

class LLMError(Exception):
    """Custom exception for LLM-related errors"""
    pass

@functools.lru_cache(maxsize=1)
def get_model():
    """
    Returns a configured Gemini model instance.
    Uses caching to avoid repeated initialization.
    """
    settings = get_settings()

    if not settings.gemini_api_key:
        raise LLMError("GEMINI_API_KEY not found in environment variables")

    try:
        genai.configure(api_key=settings.gemini_api_key)
        model = genai.GenerativeModel(settings.model_name)
        logger.info(f"Successfully initialized {settings.model_name}")
        return model
    except Exception as e:
        logger.error(f"Failed to initialize LLM model: {e}")
        raise LLMError(f"Failed to initialize LLM model: {e}")

def generate_with_retry(model, prompt, generation_config=None, max_retries=3, delay=1):
    """
    Generate content with retry logic for handling API failures.
    """
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            return response
        except Exception as e:
            logger.warning(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(delay * (2 ** attempt))  # Exponential backoff
            else:
                raise LLMError(f"Failed to generate content after {max_retries} attempts: {e}")