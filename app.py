import gradio as gr
from dotenv import load_dotenv
from analyzer.resume_service import analyze_resume as analyze_resume_service

# ==========================================================
# Theme
# ==========================================================

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="cyan",
    neutral_hue="slate"
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

    with gr.Row():
        skill_chart_image = gr.Image(
            label="🥧 Skill Matching Chart",
            type="filepath"
        )

        ats_chart_image = gr.Image(
            label="📊 ATS Breakdown Chart",
            type="filepath"
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
        fn=analyze_resume_service,
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
            skill_chart_image,
            ats_chart_image,
            ai_feedback_box
        ]
    )

# ==========================================================
# Launch
# ==========================================================

if __name__ == "__main__":
    demo.launch()