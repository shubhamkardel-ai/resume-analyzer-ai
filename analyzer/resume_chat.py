from analyzer.pdf_reader import extract_text_from_pdf


def extract_section(text, section):
    upper_text = text.upper()
    section = section.upper()

    start = upper_text.find(section)

    if start == -1:
        return f"{section} section not found."

    headings = [
        "EDUCATION",
        "EXPERIENCE",
        "PROJECTS",
        "SKILLS",
        "CERTIFICATIONS"
    ]

    end = len(text)

    for heading in headings:
        if heading == section:
            continue

        pos = upper_text.find(heading, start + len(section))

        if pos != -1 and pos < end:
            end = pos

    return text[start:end].strip()


def ask_resume(pdf, question):

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    print("Resume text length:", len(resume_text))
    print(resume_text)

    question = question.lower()

    if "skill" in question:
        return extract_section(resume_text, "SKILLS")

    elif "project" in question:
        return extract_section(resume_text, "PROJECTS")

    elif "education" in question:
        return extract_section(resume_text, "EDUCATION")


    elif "experience" in question or "summary" in question:
        return resume_text

    else:
        return (
            "Try asking:\n\n"
            "• What are my skills?\n"
            "• What projects have I built?\n"
            "• Summarize my experience.\n"
            "• What is my education?"
        )