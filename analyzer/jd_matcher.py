from analyzer.skill_extractor import extract_skills

# ==========================================================
# Skill Weights
# ==========================================================

SKILL_WEIGHTS = {

    # Programming
    "python": 10,
    "java": 6,
    "c": 4,
    "c++": 5,
    "c#": 4,
    "javascript": 4,
    "typescript": 4,

    # AI / ML
    "machine learning": 10,
    "deep learning": 9,
    "artificial intelligence": 9,
    "data science": 8,
    "scikit-learn": 8,
    "tensorflow": 8,
    "keras": 7,
    "pytorch": 8,
    "xgboost": 7,
    "lightgbm": 7,

    # Computer Vision
    "computer vision": 9,
    "opencv": 8,
    "yolo": 8,
    "mediapipe": 6,

    # NLP / LLM
    "transformers": 8,
    "bert": 7,
    "langchain": 7,
    "llm": 7,
    "generative ai": 8,
    "prompt engineering": 7,
    "rag": 6,
    "vector database": 6,

    # Backend
    "fastapi": 6,
    "flask": 5,
    "django": 6,
    "rest api": 5,

    # Data & Databases
    "sql": 8,
    "mysql": 6,
    "postgresql": 6,
    "mongodb": 6,
    "sqlite": 5,

    "numpy": 8,
    "pandas": 8,
    "matplotlib": 5,
    "seaborn": 5,
    "plotly": 5,

    # Visualization
    "power bi": 6,
    "tableau": 5,
    "excel": 5,
    "power query": 5,
    "dax": 5,

    # Cloud
    "aws": 5,
    "azure": 5,
    "gcp": 5,

    # DevOps
    "docker": 5,
    "kubernetes": 5,

    # Tools
    "git": 4,
    "github": 3,
    "pycharm": 3,
    "jupyter notebook": 3,
    "google colab": 3,
    "vscode": 3,

    # Libraries
    "pygame": 4,
    "streamlit": 4,
    "gradio": 4,
}


# ==========================================================
# Job Matcher
# ==========================================================

def match_resume_with_job(resume_text, job_description):
    """
    Compare resume skills with job description skills
    and calculate a weighted match score.
    """

    resume_skills = {
        skill.lower()
        for skill in extract_skills(resume_text)
    }

    job_skills = {
        skill.lower()
        for skill in extract_skills(job_description)
    }

    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)

    if not job_skills:
        return {
            "score": 0,
            "matched": [],
            "missing": [],
            "resume_skills": len(resume_skills),
            "job_skills": 0,
            "matched_count": 0,
            "missing_count": 0,
        }

    total_weight = sum(
        SKILL_WEIGHTS.get(skill, 3)
        for skill in job_skills
    )

    matched_weight = sum(
        SKILL_WEIGHTS.get(skill, 3)
        for skill in matched
    )

    score = round((matched_weight / total_weight) * 100)

    return {
        "score": score,
        "matched": [skill.title() for skill in matched],
        "missing": [skill.title() for skill in missing],
        "resume_skills": len(resume_skills),
        "job_skills": len(job_skills),
        "matched_count": len(matched),
        "missing_count": len(missing),
    }