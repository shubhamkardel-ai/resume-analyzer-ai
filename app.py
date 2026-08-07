import gradio as gr
from dotenv import load_dotenv
from analyzer.resume_service import analyze_resume as analyze_resume_service
from analyzer.interview_service import start_interview
from analyzer.resume_chat_service import resume_chat
from analyzer.interview_feedback import evaluate_answer
from analyzer.interview_session import next_question
from analyzer.resume_optimizer import optimize_resume

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

    with gr.Tabs():

        # ==========================================================
        # Resume Analyzer Tab
        # ==========================================================
        with gr.Tab("📊 Resume Analyzer"):

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

                interview_score = gr.Number(label="🏆 Overall Interview Score")
                technical_score = gr.Number(label="💻 Technical Score")
                communication_score = gr.Number(label="🗣 Communication Score")
                confidence_score = gr.Number(label="🔥 Confidence Score")

            questions = gr.Markdown(
                label="📋 AI Interview Questions"
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
                    label="🥧 Skill Match Chart",
                    type="filepath"
                )

                ats_chart_image = gr.Image(
                    label="📊 ATS Breakdown Chart",
                    type="filepath"
                )

            ai_feedback_box = gr.Markdown(
                label="🤖 AI Career Coach"
            )

            # ==========================================================
            # AI Resume Optimizer
            # ==========================================================

            gr.Markdown("## ✨ AI Resume Optimizer")

            optimize_btn = gr.Button(
                "✨ Optimize Resume",
                variant="primary"
            )

            optimized_resume_box = gr.Markdown(
                label="✨ Optimized Resume"
            )

            optimize_btn.click(
                fn=optimize_resume,
                inputs=[
                    resume_file,
                    job_description
                ],
                outputs=[
                    optimized_resume_box
                ]
            )

            # ==========================================================
            # AI Cover Letter
            # ==========================================================

            gr.Markdown("## 💌 AI Cover Letter")

            cover_letter_box = gr.Markdown(
                label="💌 AI Cover Letter"
            )

            report_file = gr.File(
                label="📄 Download ATS Report"
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
                    ats_score_box,
                    job_match_box,
                    resume_skill_count,
                    job_skill_count,
                    matched_skill_count,
                    missing_skill_count,
                    detected_skills,
                    matched_skills,
                    missing_skills,
                    ats_feedback,
                    ats_breakdown_box,
                    skill_chart_image,
                    ats_chart_image,
                    ai_feedback_box,
                    cover_letter_box,
                    report_file,
                    resume_preview
                ]
            )

        with gr.Tab("🎤 AI Interview Coach"):
            gr.Markdown("""
        # 🎤 AI Interview Coach

        Practice AI-generated interview questions based on your resume.
        """)


            with gr.Row():
                interview_resume = gr.File(
                    label="📄 Upload Resume (PDF)",
                    file_types=[".pdf"]
                )

                interview_job_description = gr.Textbox(
                    label="📝 Job Description",
                    lines=10,
                    placeholder="Paste the target job description..."
                )

            start_btn = gr.Button(
                "🚀 Start Interview",
                variant="primary"
            )

            next_btn = gr.Button(
                "➡️ Next Question"
            )

            gr.Markdown("---")

            with gr.Row():
                interview_score = gr.Number(
                    label="🏆 Overall Score"
                )

                technical_score = gr.Number(
                    label="💻 Technical"
                )

                communication_score = gr.Number(
                    label="🗣 Communication"
                )

                confidence_score = gr.Number(
                    label="🔥 Confidence"
                )

            questions = gr.Markdown(
                label="❓ AI Interview Questions"
            )

            answer_box = gr.Textbox(
                label="💬 Your Answer",
                lines=8,
                placeholder="Type your answer here..."
            )

            evaluate_btn = gr.Button(
                "✅ Evaluate Answer",
                variant="primary"
            )

            feedback_box = gr.Markdown(
                label="🤖 AI Interview Feedback"
            )

            start_btn.click(
                fn=start_interview,
                inputs=[
                    interview_resume,
                    interview_job_description
                ],
                outputs=[
                    interview_score,
                    technical_score,
                    communication_score,
                    confidence_score,
                    questions
                ]
            )

            next_btn.click(
                fn=next_question,
                inputs=[],
                outputs=[questions]
            )

            evaluate_btn.click(
                fn=evaluate_answer,
                inputs=[
                    questions,
                    answer_box
                ],
                outputs=[
                    feedback_box
                ]
            )

        with gr.Tab("💬 Resume Chat"):
            gr.Markdown(
                """
        # 💬 AI Resume Chat

        Ask questions about your resume.
                """
            )

            with gr.Row():
                chat_resume = gr.File(
                    label="📄 Upload Resume (PDF)",
                    file_types=[".pdf"]
                )

                question = gr.Textbox(
                    label="❓ Ask a Question",
                    placeholder="Example: What are my skills?"
                )

            ask_btn = gr.Button(
                "💬 Ask AI",
                variant="primary"
            )

            feedback_box = gr.Markdown(
                label="🤖 AI Feedback"
            )

            answer = gr.Markdown(
                label="🤖 AI Response"
            )

            ask_btn.click(
                fn=resume_chat,
                inputs=[
                    chat_resume,
                    question
                ],
                outputs=[
                    answer
                ]
            )

# ==========================================================
# Launch
# ==========================================================

if __name__ == "__main__":
    print("THIS IS MY APP")
    demo.launch()