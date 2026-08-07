import re

from analyzer.llm_service import ask_llm


def evaluate_answer(question, answer):
    """
    Evaluates a user's interview answer using an LLM.

    Returns:
        overall_score,
        technical_score,
        communication_score,
        confidence_score,
        feedback
    """

    if not answer or not answer.strip():
        return (
            0,
            0,
            0,
            0,
            "⚠️ Please enter your answer before evaluating."
        )

    prompt = f"""
You are an expert AI Technical Interviewer.

Evaluate the candidate's answer.

Interview Question:
{question}

Candidate Answer:
{answer}

Give your response in exactly this format:

Technical Score: 8/10
Communication Score: 7/10
Confidence Score: 6/10

Strengths:
- ...

Improvements:
- ...

Overall Feedback:
...
"""

    feedback = ask_llm(prompt)

    # -----------------------------------------
    # Extract scores from LLM response
    # -----------------------------------------

    technical_match = re.search(
        r"Technical Score:\s*(\d+(?:\.\d+)?)\s*/\s*10",
        feedback,
        re.IGNORECASE
    )

    communication_match = re.search(
        r"Communication Score:\s*(\d+(?:\.\d+)?)\s*/\s*10",
        feedback,
        re.IGNORECASE
    )

    confidence_match = re.search(
        r"Confidence Score:\s*(\d+(?:\.\d+)?)\s*/\s*10",
        feedback,
        re.IGNORECASE
    )

    technical_score = (
        float(technical_match.group(1))
        if technical_match
        else 0
    )

    communication_score = (
        float(communication_match.group(1))
        if communication_match
        else 0
    )

    confidence_score = (
        float(confidence_match.group(1))
        if confidence_match
        else 0
    )

    # -----------------------------------------
    # Calculate overall score
    # -----------------------------------------

    overall_score = round(
        (
            technical_score
            + communication_score
            + confidence_score
        ) / 3,
        1
    )

    return (
        overall_score,
        technical_score,
        communication_score,
        confidence_score,
        feedback
    )