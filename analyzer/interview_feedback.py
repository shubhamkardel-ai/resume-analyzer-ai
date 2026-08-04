from analyzer.llm_service import ask_llm


def evaluate_answer(question, answer):
    """
    Evaluates a user's interview answer using an LLM.
    """

    prompt = f"""
You are an expert AI Technical Interviewer.

Evaluate the candidate's answer.

Interview Question:
{question}

Candidate Answer:
{answer}

Give your response in exactly this format:

Technical Score: /10
Communication Score: /10
Confidence Score: /10

Strengths:
- ...

Improvements:
- ...

Overall Feedback:
...
"""

    return ask_llm(prompt)