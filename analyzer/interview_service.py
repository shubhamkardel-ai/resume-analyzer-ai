from analyzer.pdf_reader import extract_text_from_pdf


def start_interview(pdf, jd):

    if pdf is None:

        return (
            0,
            0,
            0,
            0,
            "Please upload your resume."
        )

    resume_text = extract_text_from_pdf(pdf)

    message = f"""
# ✅ Resume Loaded Successfully

Resume Length: **{len(resume_text)} characters**

Job Description Length: **{len(jd)} characters**

The AI Interview Coach is ready to generate interview questions.
"""

    return (
        0,
        0,
        0,
        0,
        message
    )