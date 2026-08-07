from analyzer.llm_service import ask_llm

def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are an expert career assistant.

Write a professional, ATS-friendly cover letter based on the candidate's resume
and the target job description.

Keep it concise and professional.
Do not invent experience, skills, companies, or achievements.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Write only the cover letter.
"""

    return ask_llm(prompt)