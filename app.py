import gradio as gr

from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills
from analyzer.ats_score import calculate_ats_score


def analyze_resume(pdf):

    if pdf is None:
        return "", "", 0, "Please upload a PDF."

    # Extract text from PDF
    text = extract_text_from_pdf(pdf)

    # Extract skills
    skills = extract_skills(text)

    if skills:
        skills_output = "\n".join(skills)
    else:
        skills_output = "No known skills detected."

    # Calculate ATS Score
    score, feedback = calculate_ats_score(text, skills)

    if feedback:
        feedback_text = "\n".join(feedback)
    else:
        feedback_text = "Excellent Resume!"

    return (
        text,
        skills_output,
        score,
        feedback_text
    )


demo = gr.Interface(
    fn=analyze_resume,

    inputs=gr.File(
        label="Upload Resume (PDF)"
    ),

    outputs=[
        gr.Textbox(
            label="Extracted Resume Text",
            lines=18
        ),

        gr.Textbox(
            label="Detected Skills",
            lines=10
        ),

        gr.Number(
            label="ATS Score"
        ),

        gr.Textbox(
            label="Suggestions",
            lines=6
        ),
    ],

    title="Resume Analyzer AI",
    description="Upload a resume and get ATS score with skill analysis."
)

demo.launch()