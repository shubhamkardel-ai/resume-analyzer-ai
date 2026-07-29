from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills
from analyzer.ats_score import calculate_ats_score
from analyzer.jd_matcher import match_resume_with_job
from analyzer.ai_feedback import generate_feedback
from analyzer.chart_generator import (
    create_skill_pie_chart,
    create_ats_bar_chart,
)


def analyze_resume(pdf, jd):

    if pdf is None:
        return (
            "",
            "",
            0,
            "Please upload a PDF.",
            "",
            0,
            0,
            0,
            0,
            0,
            "",
            "",
            None,
            None,
            ""
        )

    # ------------------------------------------------------
    # Resume Text
    # ------------------------------------------------------

    text = extract_text_from_pdf(pdf)

    # ------------------------------------------------------
    # Skills
    # ------------------------------------------------------

    skills = extract_skills(text)

    skills_output = (
        "\n".join(skills)
        if skills
        else "No technical skills detected."
    )

    # ------------------------------------------------------
    # ATS
    # ------------------------------------------------------

    ats_score, ats_feedback, ats_breakdown = calculate_ats_score(
        text,
        skills
    )

    feedback_output = (
        "\n".join(ats_feedback)
        if ats_feedback
        else "Excellent Resume!"
    )

    breakdown_output = "\n".join(
        f"{k}: {v}"
        for k, v in ats_breakdown.items()
    )

    # ------------------------------------------------------
    # Job Matching
    # ------------------------------------------------------

    job_match = 0
    matched_output = ""
    missing_output = ""
    missing_skills = []

    resume_skill_count = 0
    job_skill_count = 0
    matched_skill_count = 0
    missing_skill_count = 0

    if jd.strip():

        result = match_resume_with_job(
            text,
            jd
        )

        job_match = result["score"]

        matched_output = "\n".join(result["matched"])

        missing_output = "\n".join(result["missing"])

        missing_skills = result["missing"]

        resume_skill_count = result["resume_skills"]

        job_skill_count = result["job_skills"]

        matched_skill_count = result["matched_count"]

        missing_skill_count = result["missing_count"]

    # ------------------------------------------------------
    # Charts
    # ------------------------------------------------------

    skill_chart = create_skill_pie_chart(
        matched_skill_count,
        missing_skill_count
    )

    ats_chart = create_ats_bar_chart(
        ats_breakdown
    )

    # ------------------------------------------------------
    # AI Feedback
    # ------------------------------------------------------

    if jd.strip():

        ai_feedback = generate_feedback(
            text,
            ats_score,
            missing_skills
        )

    else:

        ai_feedback = (
            "Upload a Job Description "
            "to receive AI-powered feedback."
        )

    return (
        text,
        skills_output,
        ats_score,
        feedback_output,
        breakdown_output,
        job_match,
        resume_skill_count,
        job_skill_count,
        matched_skill_count,
        missing_skill_count,
        matched_output,
        missing_output,
        skill_chart,
        ats_chart,
        ai_feedback
    )