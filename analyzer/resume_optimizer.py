from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.llm_service import ask_llm


def optimize_resume(pdf, job_description):

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
You are an expert ATS Resume Writer.

Your task is to improve the resume for the given Job Description.

Rules:

- Do NOT invent experience.
- Do NOT invent projects.
- Do NOT invent skills.
- Rewrite existing content professionally.
- Improve ATS keywords.
- Improve formatting.
- Improve bullet points.
- Suggest stronger action verbs.
- Highlight missing keywords from the job description.
- Return the optimized resume in Markdown.

Resume:

{resume_text}

Job Description:

{job_description}

Optimized Resume:
"""

    return ask_llm(prompt)