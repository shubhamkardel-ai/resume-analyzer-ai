from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.resume_parser import extract_section


def resume_chat(pdf, question):
    """
    Simple Resume Chat Service (Version 1)

    Reads the resume and answers basic questions.
    """

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    question = question.lower()

    question = question.lower()

    if "skill" in question:
        return extract_section(resume_text, "SKILLS")

    elif "project" in question:
        return extract_section(resume_text, "PROJECTS")


    elif "experience" in question or "summary" in question:
        return extract_section(resume_text, "EXPERIENCE")

    elif "education" in question:
        return extract_section(resume_text, "EDUCATION")

    elif "certification" in question or "certificate" in question:
        return extract_section(resume_text, "CERTIFICATIONS")

    return "Please ask about Skills, Projects, Experience, Education, or Certifications."