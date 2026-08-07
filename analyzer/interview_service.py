from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills
from analyzer.interview_session import set_questions, get_current_question


def start_interview(pdf, jd):

    # ======================================================
    # Resume Validation
    # ======================================================

    if pdf is None:
        return (
            0,
            0,
            0,
            0,
            "Please upload your resume."
        )

    # ======================================================
    # Job Description Validation
    # ======================================================

    if jd is None or not jd.strip():
        return (
            0,
            0,
            0,
            0,
            "Please enter a Job Description."
        )

    # ======================================================
    # Extract Resume
    # ======================================================

    resume_text = extract_text_from_pdf(pdf)

    resume_skills = extract_skills(resume_text)

    # ======================================================
    # Extract Job Description Skills
    # ======================================================

    jd_skills = extract_skills(jd)

    # ======================================================
    # Find Matched Skills
    # ======================================================

    matched_skills = []

    for skill in resume_skills:
        if skill in jd_skills:
            matched_skills.append(skill)

    # ======================================================
    # Generate Interview Questions
    # ======================================================

    questions = []

    for skill in matched_skills[:5]:

        questions.append(
            f"• Explain your experience with {skill}."
        )

        questions.append(
            f"• Describe a project where you used {skill}."
        )

        questions.append(
            f"• What challenges did you face while using {skill}?"
        )

    # ======================================================
    # Store Questions
    # ======================================================

    set_questions(questions)

    question_text = get_current_question()

    # ======================================================
    # Interview Message
    # ======================================================

    message = f"""
# ✅ Resume Loaded Successfully

Resume Length: **{len(resume_text)} characters**

Job Description Length: **{len(jd)} characters**

Matched Skills: **{len(matched_skills)}**

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