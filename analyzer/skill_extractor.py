# analyzer/skill_extractor.py

SKILLS = [
    "Python",
    "SQL",
    "Power BI",
    "Excel",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "FastAPI",
    "Flask",
    "OpenCV",
    "NLP",
    "Computer Vision",
    "Generative AI",
    "LLM",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "Linux",
]


def extract_skills(text):
    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(found_skills)