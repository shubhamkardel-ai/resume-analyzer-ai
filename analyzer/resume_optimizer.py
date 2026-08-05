from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.llm_service import ask_llm


def optimize_resume(pdf, job_description):

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
You are an expert ATS Resume Writer.

Rewrite the resume to better match the given Job Description.

Rules:

- Never invent experience.
- Never invent projects.
- Never invent certifications.
- Never invent skills.
- Improve wording.
- Improve ATS keywords.
- Improve formatting.
- Improve bullet points.
- Keep everything truthful.
- Return the optimized resume in Markdown.

Resume:

{resume_text}

Job Description:

{job_description}

Optimized Resume:
"""

    return ask_llm(prompt)