from analyzer.pdf_reader import extract_text_from_pdf


def ask_resume(pdf, question):

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    question = question.lower()

    if "skill" in question:
        return resume_text[:1000]

    elif "project" in question:
        return resume_text[:1000]

    elif "education" in question:
        return resume_text[:1000]

    elif "experience" in question:
        return resume_text[:1000]

    else:
        return (
            "I found your resume successfully.\n\n"
            "Try asking:\n"
            "• What are my skills?\n"
            "• Tell me about my projects.\n"
            "• Summarize my resume.\n"
            "• What experience do I have?"
        )