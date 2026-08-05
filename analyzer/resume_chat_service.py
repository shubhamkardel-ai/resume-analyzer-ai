from analyzer.pdf_reader import extract_text_from_pdf
from analyzer.llm_service import ask_llm


def resume_chat(pdf, question):

    if pdf is None:
        return "Please upload your resume."

    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
    You are an expert AI Resume Assistant.

    Use ONLY the information contained in the resume below.

    Rules:
    - Never invent information.
    - If the answer is not present, say:
      "I couldn't find that information in the resume."
    - Keep answers concise and professional.
    - Use bullet points whenever appropriate.

    Resume:
    {resume_text}

    User Question:
    {question}

    Answer:
    """

    return ask_llm(prompt)