import gradio as gr

from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.skill_extractor import extract_skills


def analyze_resume(pdf):

    if pdf is None:
        return "", "Please upload a PDF."

    text = extract_text_from_pdf(pdf)

    skills = extract_skills(text)

    if skills:
        skills_output = "\n".join(skills)
    else:
        skills_output = "No known skills detected."

    return text, skills_output


demo = gr.Interface(
    fn=analyze_resume,
    inputs=gr.File(label="Upload Resume"),
    outputs=[
        gr.Textbox(label="Extracted Resume Text", lines=18),
        gr.Textbox(label="Detected Skills", lines=10),
    ],
    title="Resume Analyzer AI",
    description="Upload your resume to extract text and identify technical skills.",
)

demo.launch()