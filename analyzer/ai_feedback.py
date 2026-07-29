import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# ==========================================================
# Configuration
# ==========================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_NAME = os.getenv(
    "HF_MODEL",
    "Qwen/Qwen2.5-7B-Instruct-1M"
)


# ==========================================================
# Hugging Face Client
# ==========================================================

client = InferenceClient(
    api_key=HF_TOKEN
)


# ==========================================================
# AI Resume Feedback
# ==========================================================

def generate_feedback(
    resume_text,
    ats_score,
    missing_skills
):
    """
    Generate AI-powered resume improvement suggestions.

    Parameters
    ----------
    resume_text : str
        Extracted resume text.

    ats_score : int
        Calculated ATS score.

    missing_skills : list
        Skills missing from the resume based on
        the provided job description.

    Returns
    -------
    str
        AI-generated resume feedback.
    """

    # ------------------------------------------------------
    # Check Hugging Face Token
    # ------------------------------------------------------

    if not HF_TOKEN:
        return (
            "WARNING: Hugging Face API token not found.\n\n"
            "Please create a .env file and add:\n\n"
            "HF_TOKEN=your_token"
        )

    # ------------------------------------------------------
    # Prepare Missing Skills
    # ------------------------------------------------------

    missing_skills_text = (
        ", ".join(missing_skills)
        if missing_skills
        else "None"
    )

    # ------------------------------------------------------
    # Build Prompt
    # ------------------------------------------------------

    prompt = f"""
You are an experienced ATS Resume Reviewer and AI Career Coach.

Analyze the candidate's resume.

ATS Score:
{ats_score}/100

Missing Skills:
{missing_skills_text}

Resume:
{resume_text[:2500]}

Provide a professional analysis with these sections:

1. Overall Evaluation
2. Five ATS Improvement Suggestions
3. Missing Technical Skills
4. Resume Formatting Advice
5. Final Career Recommendation

Keep the response concise, practical, and professional.

Focus on actionable advice that can help the candidate
improve their chances of passing ATS screening.
"""

    # ------------------------------------------------------
    # Generate AI Response
    # ------------------------------------------------------

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500
        )

        return response.choices[0].message.content

    # ------------------------------------------------------
    # Handle API Errors
    # ------------------------------------------------------

    except Exception as e:

        return (
            "AI feedback is currently unavailable.\n\n"
            f"Error:\n{str(e)}"
        )