import gradio as gr

from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills
from analyzer.ats_score import calculate_ats_score
from analyzer.jd_matcher import match_resume_with_job
from analyzer.ai_feedback import generate_feedback

# ==========================================================
# Theme
# ==========================================================

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="cyan",
    neutral_hue="slate"
)

# ==========================================================
# Resume Analyzer
# ==========================================================

def analyze_resume(pdf, jd):

    if pdf is None:
        return (
            "",
            "",
            0,
            "Please upload a PDF.",
            0,
            "No Job Description Provided",
            ""
        )

    # ------------------------------------------------------
    # Extract Resume Text
    # ------------------------------------------------------

    text = extract_text_from_pdf(pdf)

    # ------------------------------------------------------
    # Extract Skills
    # ------------------------------------------------------

    skills = extract_skills(text)

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

    feedback_output = (
        "\n".join(ats_feedback)
        if ats_feedback
        else "Excellent Resume!"
    )

    breakdown_output = ""

    for key, value in ats_breakdown.items():
        breakdown_output += f"{key:<20}: {value}\n"

    # ------------------------------------------------------
    # Job Matching
    # ------------------------------------------------------

    job_match = 0
    missing_output = "No Job Description Provided"
    missing_skills = []
    resume_skill_count = 0
    job_skill_count = 0
    matched_skill_count = 0
    missing_skill_count = 0
    matched_output = "No Job Description Provided"

    if jd.strip():
        result = match_resume_with_job(
            text,
            jd
        )

        job_match = result["score"]

        missing_skills = result["missing"]

        matched_skills = result["matched"]

        matched_output = (
            "\n".join(matched_skills)
            if matched_skills
            else "No matching skills found."
        )

        resume_skill_count = result["resume_skills"]

        job_skill_count = result["job_skills"]

        matched_skill_count = result["matched_count"]

        missing_skill_count = result["missing_count"]

        missing_output = (
            "\n".join(missing_skills)
            if missing_skills
            else "Perfect Match!"
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
            "Upload a Job Description to receive AI-powered feedback."
        )

    # ------------------------------------------------------
    # Return Outputs
    # ------------------------------------------------------

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
        ai_feedback
    )


# ==========================================================
# User Interface
# ==========================================================

with gr.Blocks(
    theme=theme,
    title="Resume Analyzer AI"
) as demo:

    gr.Markdown(
        """
# 🚀 Resume Analyzer AI

### AI-Powered ATS Screening • Skill Detection • Job Matching • AI Career Coach

Analyze resumes against job descriptions using NLP-based skill extraction,
ATS scoring, intelligent job matching, and AI-powered resume feedback.

---
"""
    )

    with gr.Row():

        resume_file = gr.File(
            label="📄 Upload Resume (PDF)",
            file_types=[".pdf"]
        )

        job_description = gr.Textbox(
            label="📝 Paste Job Description",
            lines=12,
            placeholder="Paste the job description here..."
        )

    gr.Markdown("## 📊 Analysis Dashboard")

    analyze_btn = gr.Button(
        "🚀 Analyze Resume",
        variant="primary"
    )

    with gr.Row():
        with gr.Column():
            ats_score_box = gr.Slider(
                minimum=0,
                maximum=100,
                step=1,
                value=0,
                interactive=False,
                label="📊 ATS Score (/100)"
            )

            job_match_box = gr.Slider(
                minimum=0,
                maximum=100,
                step=1,
                value=0,
                interactive=False,
                label="🎯 Job Match (%)"
            )

            resume_skill_count = gr.Number(
                label="📄 Resume Skills"
            )

            job_skill_count = gr.Number(
                label="💼 Job Skills"
            )

        with gr.Column():
            matched_skill_count = gr.Number(
                label="✅ Matched Skills"
            )

            missing_skill_count = gr.Number(
                label="❌ Missing Skills"
            )

            detected_skills = gr.Textbox(
                label="🛠 Detected Technical Skills",
                lines=10
            )

            matched_skills = gr.Textbox(
                label="✅ Matched Skills",
                lines=10
            )

            missing_skills = gr.Textbox(
                label="⚠ Missing Skills",
                lines=10
            )

    ats_feedback = gr.Textbox(
        label="📋 ATS Suggestions",
        lines=8
    )

    ats_breakdown_box = gr.Textbox(
        label="📊 ATS Score Breakdown",
        lines=10
    )

    ai_feedback_box = gr.Textbox(
        label="🤖 AI Career Coach",
        lines=14
    )

    resume_preview = gr.Textbox(
        label="📄 Resume Preview",
        lines=20
    )

    analyze_btn.click(
        fn=analyze_resume,
        inputs=[
            resume_file,
            job_description
        ],
        outputs=[
            resume_preview,
            detected_skills,
            ats_score_box,
            ats_feedback,
            ats_breakdown_box,
            job_match_box,
            resume_skill_count,
            job_skill_count,
            matched_skill_count,
            missing_skill_count,
            matched_skills,
            missing_skills,
            ai_feedback_box
        ]
    )

# ==========================================================
# Launch
# ==========================================================

if __name__ == "__main__":
    demo.launch()