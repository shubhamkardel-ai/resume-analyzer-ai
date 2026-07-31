from analyzer.llm_client import generate_text

def generate_cover_letter(resume, job_description):
    """
    Generate a professional AI cover letter.
    """

    prompt = f"""
You are an expert HR recruiter.

Write a professional one-page cover letter.

Rules:

- Use the candidate's resume.
- Match the job description.
- Be professional.
- Keep it ATS-friendly.
- Do NOT invent experience.
- Return only the cover letter in Markdown.

Resume:

{resume}

Job Description:

{job_description}
"""

    return generate_text(prompt)