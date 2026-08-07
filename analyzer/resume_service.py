from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills
from analyzer.ats_score import calculate_ats_score
from analyzer.jd_matcher import match_resume_with_job
from analyzer.ai_feedback import generate_feedback
from analyzer.optimizer import optimize_resume
from analyzer.report_generator import generate_report
from analyzer.cover_letter import generate_cover_letter
from analyzer.chart_generator import (
    create_skill_pie_chart,
    create_ats_bar_chart,
)


def analyze_resume(pdf, jd):

    if pdf is None:
        return (
            0,                  # ATS Score
            0,                  # Job Match
            0,                  # Resume Skills
            0,                  # Job Skills
            0,                  # Matched Skills
            0,                  # Missing Skills
            "",                 # Skills Output
            "",                 # Matched Output
            "",                 # Missing Output
            "Please upload a PDF.",
            "",
            None,
            None,
            "",
            "",
            "",
            None,
            "",
        )

    # ------------------------------------------------------
    # Resume Text
    # ------------------------------------------------------

    text = extract_text_from_pdf(pdf)
    print("1. PDF Extracted")

    # ------------------------------------------------------
    # Skill Extraction
    # ------------------------------------------------------

    skills = extract_skills(text)
    print("2. Skills Extracted")

    skills_output = (
        "\n".join(skills)
        if skills
        else "No technical skills detected."
    )

    # ------------------------------------------------------
    # ATS Score
    # ------------------------------------------------------

    ats_score, ats_feedback, ats_breakdown = calculate_ats_score(
        text,
        skills
    )

    print("3. ATS Calculated")

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
    # Default Values
    # ------------------------------------------------------

    job_match = 0

    matched_output = ""
    missing_output = ""
    missing_skills = []

    resume_skill_count = 0
    job_skill_count = 0
    matched_skill_count = 0
    missing_skill_count = 0

    ai_feedback = ""
    optimized_resume = ""
    cover_letter = ""
    report_path = None

    # ------------------------------------------------------
    # Job Matching + AI
    # ------------------------------------------------------

    if jd.strip():

        result = match_resume_with_job(
            text,
            jd
        )

        print("4. Job Matching Done")

        job_match = result["score"]

        matched_output = "\n".join(
            result["matched"]
        )

        missing_output = "\n".join(
            result["missing"]
        )

        missing_skills = result["missing"]

        resume_skill_count = result["resume_skills"]
        job_skill_count = result["job_skills"]
        matched_skill_count = result["matched_count"]
        missing_skill_count = result["missing_count"]

        print("5. Generating AI Feedback...")

        ai_feedback = generate_feedback(
            text,
            ats_score,
            missing_skills
        )

        print("6. AI Feedback Done")

        optimized_resume = ""

        cover_letter = ""

        report_path = None

    else:

        ai_feedback = (
            "Upload a Job Description "
            "to receive AI-powered feedback."
        )

        optimized_resume = ""
        cover_letter = ""
        report_path = None

    # ------------------------------------------------------
    # Charts
    # ------------------------------------------------------

    skill_chart = create_skill_pie_chart(
        matched_skill_count,
        missing_skill_count
    )

    print("5. Skill Chart Done")

    ats_chart = create_ats_bar_chart(
        ats_breakdown
    )

    print("6. ATS Chart Done")

    print("Charts Created")

    print("Skill Chart:", skill_chart)
    print("ATS Chart:", ats_chart)
    print(type(skill_chart))
    print(type(ats_chart))

    # ------------------------------------------------------
    # Return
    # ------------------------------------------------------

    print("Returning to Gradio")

    return (
        ats_score,
        job_match,
        resume_skill_count,
        job_skill_count,
        matched_skill_count,
        missing_skill_count,
        skills_output,
        matched_output,
        missing_output,
        feedback_output,
        breakdown_output,
        skill_chart,
        ats_chart,
        ai_feedback,
        optimized_resume,
        cover_letter,
        report_path,
        text,
    )