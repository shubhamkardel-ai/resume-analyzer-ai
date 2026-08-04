from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.llm_service import ask_llm


def resume_chat(pdf, question):

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
You are an AI Resume Assistant.

Answer the user's question ONLY using the resume below.

If the answer is not available in the resume, reply:
"I couldn't find that information in the resume."

Resume:
{resume_text}

Question:
{question}

Answer:
"""

    return ask_llm(prompt)