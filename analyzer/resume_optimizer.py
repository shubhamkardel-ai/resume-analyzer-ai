from analyzer.llm_client import generate_text
from analyzer.pdf_reader import extract_text_from_pdf


def optimize_resume(pdf, job_description):

    if pdf is None:
        return "Please upload a resume PDF."

    if not job_description.strip():
        return "Please provide a Job Description."

    # Extract resume text
    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
    You are an expert ATS resume editor.

    Your task is to REWRITE THE RESUME, NOT write a cover letter.

    RESUME:
    {resume_text}

    TARGET JOB DESCRIPTION:
    {job_description}

    STRICT OUTPUT RULES:

    1. Return ONLY the optimized resume.
    2. NEVER write a cover letter.
    3. NEVER start with "Dear Hiring Manager".
    4. NEVER use "Sincerely".
    5. NEVER write "I am excited to apply".
    6. Do NOT write an introduction letter.
    7. Do NOT invent any skills, experience, projects, education, or achievements.
    8. Only improve the wording, structure, formatting, and ATS keyword alignment.
    9. Keep all real information from the original resume.
    10. Add job-description keywords ONLY when they are genuinely supported by the resume.
    11. Use strong action verbs in experience and project descriptions.
    12. Improve the Skills section for ATS readability.
    13. Keep the resume concise and professional.

    RETURN THE RESUME IN THIS STRUCTURE:

    NAME
    CONTACT INFORMATION

    EDUCATION
    ...

    EXPERIENCE
    ...

    PROJECTS
    ...

    SKILLS
    ...

    CERTIFICATIONS
    ...

    IMPORTANT:
    Your entire response must be a RESUME.
    Do not provide explanations.
    Do not provide suggestions.
    Do not provide a cover letter.
    Do not mention these instructions.

    Now rewrite the resume:
    """

    print("7. Generating Optimized Resume...")

    optimized_resume = generate_text(prompt)

    print("8. Optimized Resume Done")

    return optimized_resume