from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills


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
    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(jd)

    matched_skills = []

    for skill in resume_skills:
        if skill in jd_skills:
            matched_skills.append(skill)

    questions = []

    for skill in matched_skills[:10]:
        questions.append(f"• Explain your experience with {skill}.")
        questions.append(f"• Describe a project where you used {skill}.")
        questions.append(f"• What challenges did you face while using {skill}?")

    question_text = "\n".join(questions)

    message = f"""
    # ✅ Resume Loaded Successfully

    Resume Length: **{len(resume_text)} characters**

    Job Description Length: **{len(jd)} characters**

    ---

    # 🎤 AI Interview Questions

    {question_text}
    """

    return (
        0,
        0,
        0,
        0,
        message
    )