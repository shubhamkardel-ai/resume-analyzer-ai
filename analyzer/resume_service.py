from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills
from analyzer.ats_score import calculate_ats_score
from analyzer.jd_matcher import match_resume_with_job

from analyzer.ai_feedback import generate_feedback
from analyzer.cover_letter import generate_cover_letter
from analyzer.report_generator import generate_report

from analyzer.chart_generator import (
    create_skill_pie_chart,
    create_ats_bar_chart,
)


def analyze_resume(pdf, jd):

    # ======================================================
    # Default / Empty State
    # ======================================================

    if pdf is None:
        return (
            0,
            0,
            0,
            0,
            0,
            0,
            "",
            "",
            "",
            "Please upload a PDF.",
            "",
            None,
            None,
            "",
            "",
            None,
            "",
        )

    # ======================================================
    # 1. Extract Resume Text
    # ======================================================

    text = extract_text_from_pdf(pdf)

    print("1. PDF Extracted")

    # ======================================================
    # 2. Extract Skills
    # ======================================================

    skills = extract_skills(text)

    print("2. Skills Extracted")

    skills_output = (
        "\n".join(skills)
        if skills
        else "No technical skills detected."
    )

    # ======================================================
    # 3. ATS Score
    # ======================================================

    ats_score, ats_feedback, ats_breakdown = calculate_ats_score(
        text,
        skills
    )

    print("3. ATS Calculated")

    feedback_output = (
        "\n".join(ats_feedback)
        if ats_feedback
        else "Excellent resume structure and ATS optimization."
    )

    breakdown_output = "\n".join(
        f"{key}: {value}"
        for key, value in ats_breakdown.items()
    )

    # ======================================================
    # 4. Default Values
    # ======================================================

    job_match = 0

    matched_output = ""
    missing_output = ""

    resume_skill_count = 0
    job_skill_count = 0
    matched_skill_count = 0
    missing_skill_count = 0

    ai_feedback = ""
    cover_letter = ""

    report_path = None

    # ======================================================
    # 5. Job Matching
    # ======================================================

    if jd and jd.strip():

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

        resume_skill_count = result["resume_skills"]

        job_skill_count = result["job_skills"]

        matched_skill_count = result["matched_count"]

        missing_skill_count = result["missing_count"]

        # ==================================================
        # 5A. AI Career Coach
        # ==================================================

        print("5. Generating AI Feedback...")

        try:

            ai_feedback = generate_feedback(
                text,
                ats_score,
                result["missing"]
            )

            print("5. AI Feedback Done")

        except Exception as e:

            print(
                "AI Feedback Error:",
                e
            )

            ai_feedback = (
                "AI Career Coach is currently unavailable."
            )

        # ==================================================
        # 5B. Cover Letter
        # ==================================================

        print("6. Generating Cover Letter...")

        try:

            cover_letter = generate_cover_letter(
                text,
                jd
            )

            print("6. Cover Letter Done")

        except Exception as e:

            print(
                "Cover Letter Error:",
                e
            )

            cover_letter = (
                "Cover letter generation is currently unavailable."
            )

    else:

        ai_feedback = (
            "Upload a Job Description "
            "to receive AI-powered feedback."
        )

    # ======================================================
    # 7. Generate Skill Chart
    # ======================================================

    skill_chart = create_skill_pie_chart(
        matched_skill_count,
        missing_skill_count
    )

    print("7. Skill Chart Done")

    # ======================================================
    # 8. Generate ATS Chart
    # ======================================================

    ats_chart = create_ats_bar_chart(
        ats_breakdown
    )

    print("8. ATS Chart Done")

    # ======================================================
    # 9. Resume Preview
    # ======================================================

    resume_preview = text

    # ======================================================
    # 10. Generate ATS Report
    # ======================================================

    print("9. Generating ATS Report...")

    try:

        report_path = generate_report(
            ats_score=ats_score,
            job_match=job_match,
            matched_skills=matched_output,
            missing_skills=missing_output,
            ats_breakdown=breakdown_output,
            ai_feedback=ai_feedback,
            optimized_resume=""
        )

        print(
            "10. ATS Report Done:",
            report_path
        )

    except Exception as e:

        print(
            "ATS Report Error:",
            e
        )

        report_path = None

    # ======================================================
    # 11. Final Return
    # ======================================================

    print("Returning to Gradio")

    return (
        ats_score,             # 1
        job_match,             # 2
        resume_skill_count,    # 3
        job_skill_count,       # 4
        matched_skill_count,   # 5
        missing_skill_count,   # 6
        skills_output,         # 7
        matched_output,        # 8
        missing_output,        # 9
        feedback_output,       # 10
        breakdown_output,      # 11
        skill_chart,           # 12
        ats_chart,             # 13
        ai_feedback,           # 14
        cover_letter,          # 15
        report_path,           # 16
        resume_preview         # 17
    )