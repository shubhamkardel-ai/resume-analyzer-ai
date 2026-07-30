from analyzer.llm_client import generate_text

def optimize_resume(text):
    """
    Uses the LLM to rewrite the resume professionally
    while keeping all information truthful.
    """

    prompt = f"""
You are an expert ATS Resume Writer.

Rewrite the following resume professionally.

Rules:

- Improve grammar.
- Improve readability.
- Use strong ATS keywords.
- Use strong action verbs.
- Improve bullet points.
- Add measurable achievements ONLY if they are implied.
- Do NOT invent fake companies, fake skills, fake projects or fake experience.
- Keep everything truthful.
- Return ONLY the improved resume in Markdown format.

Resume:

{text}
"""

    return generate_text(prompt)