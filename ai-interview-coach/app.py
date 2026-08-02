import gradio as gr

# ----------------------------
# Theme
# ----------------------------

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="cyan",
    neutral_hue="slate"
)

# ----------------------------
# UI
# ----------------------------

with gr.Blocks(
    theme=theme,
    title="AI Interview Coach"
) as demo:

    gr.Markdown(
        """
# 🎤 AI Interview Coach

### AI-Powered Mock Interviews • Resume-Based Questions • AI Evaluation • Interview Reports
        """
    )

    with gr.Row():

        resume = gr.File(
            label="📄 Upload Resume (PDF)",
            file_types=[".pdf"]
        )

        job_description = gr.Textbox(
            label="📝 Job Description",
            lines=18,
            placeholder="Paste the job description here..."
        )

    start_btn = gr.Button(
        "🚀 Start Interview",
        variant="primary"
    )

    gr.Markdown("---")

    with gr.Row():

        interview_score = gr.Number(
            label="🎯 Interview Score"
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
        label="❓ Interview Questions"
    )

    answer = gr.Textbox(
        label="✍ Your Answer",
        lines=8,
        placeholder="Write your answer here..."
    )

    evaluate_btn = gr.Button(
        "✅ Evaluate Answer"
    )

    feedback = gr.Markdown(
        label="🤖 AI Feedback"
    )

demo.launch()