import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# ==========================================================
# Hugging Face Client
# ==========================================================

client = InferenceClient(
    api_key=HF_TOKEN
)

# ==========================================================
# AI Resume Feedback
# ==========================================================

def generate_feedback(resume_text, ats_score, missing_skills):
    """
    Generate AI-based resume improvement suggestions.

    Parameters
    ----------
    resume_text : str
    ats_score : int
    missing_skills : list

    Returns
    -------
    str
    """

    if not HF_TOKEN:
        return (
            "⚠ Hugging Face API token not found.\n"
            "Create a .env file and add:\n\n"
            "HF_TOKEN=your_token"
        )

    prompt = f"""
You are an experienced ATS Resume Reviewer and Career Coach.

Analyze the resume below.

Current ATS Score:
{ats_score}/100

Missing Skills:
{", ".join(missing_skills) if missing_skills else "None"}

Resume:

{resume_text[:2500]}

Provide:

1. Overall evaluation.
2. Five ATS improvement suggestions.
3. Missing technical skills.
4. Resume formatting advice.
5. Final recommendation.

Respond in professional markdown.
"""

    try:

        response = client.chat.completions.create(

            model="HuggingFaceTB/SmolLM3-3B",

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            max_tokens=500,

        )

        return response.choices[0].message.content

    except Exception as e:

        return (
            "❌ AI feedback is currently unavailable.\n\n"
            f"Error:\n{e}"
        )