from analyzer.llm_client import generate_text


def generate_feedback(
    resume_text,
    ats_score,
    missing_skills
):
    """
    Generate AI-powered resume improvement suggestions.
    """

    missing_skills_text = (
        ", ".join(missing_skills)
        if missing_skills
        else "None"
    )

    prompt = f"""
You are an experienced ATS Resume Reviewer and AI Career Coach.

Analyze the candidate's resume.

ATS Score:
{ats_score}/100

Missing Skills:
{missing_skills_text}

Resume:
{resume_text[:2500]}

Provide a professional analysis with these sections:

## 1. Overall Evaluation

## 2. Five ATS Improvement Suggestions

## 3. Missing Technical Skills

## 4. Resume Formatting Advice

## 5. Final Career Recommendation

Rules:
- Be concise and practical.
- Give actionable advice.
- Use professional language.
- Complete all five sections.
- Do not stop mid-sentence.
- Do not repeat the resume.
"""

    return generate_text(prompt)