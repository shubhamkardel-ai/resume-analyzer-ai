import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# ==========================================================
# Configuration
# ==========================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("HF_MODEL")


# ==========================================================
# Hugging Face Client
# ==========================================================

_client = None

if HF_TOKEN:
    _client = InferenceClient(
        api_key=HF_TOKEN
    )


# ==========================================================
# LLM Generation
# ==========================================================

def generate_text(
    prompt: str,
    max_tokens: int = 800
) -> str:
    """
    Generate text using the configured LLM provider.

    Parameters
    ----------
    prompt : str
        Prompt sent to the language model.

    max_tokens : int
        Maximum number of tokens to generate.

    Returns
    -------
    str
        Generated response.
    """

    if not HF_TOKEN:
        return (
            "AI feedback is unavailable because the "
            "Hugging Face API token is not configured."
        )

    if not MODEL_NAME:
        return (
            "AI feedback is unavailable because "
            "HF_MODEL is not configured."
        )

    if _client is None:
        return "AI client could not be initialized."

    try:
        response = _client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=400,
            temperature=0.3,
        )

        return response.choices[0].message.content

    except Exception as e:
        return (
            "AI feedback is currently unavailable.\n\n"
            f"Error: {str(e)}"
        )