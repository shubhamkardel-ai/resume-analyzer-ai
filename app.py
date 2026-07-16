import gradio as gr

from analyzer.pdf_reader import extract_text_from_pdf


def analyze_resume(pdf):
    if pdf is None:
        return "Please upload a PDF."

    return extract_text_from_pdf(pdf)


demo = gr.Interface(
    fn=analyze_resume,
    inputs=gr.File(label="Upload Resume (PDF)"),
    outputs=gr.Textbox(
        label="Extracted Resume Text",
        lines=20
    ),
    title="Resume Analyzer AI",
    description="Upload a PDF resume and extract its text."
)

demo.launch()