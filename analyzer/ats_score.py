import re

EDUCATION = [
    "b.tech",
    "b.e",
    "bca",
    "mca",
    "m.tech",
    "msc",
    "bsc",
    "phd",
]

EXPERIENCE = [
    "intern",
    "internship",
    "developer",
    "engineer",
    "analyst",
    "experience",
]

CONTACT = [
    "@",
    "+91",
]


def calculate_ats_score(text, skills):

    score = 0
    feedback = []

    # ---------- Skills (40) ----------
    skill_score = min(len(skills) * 5, 40)
    score += skill_score

    if skill_score < 25:
        feedback.append("Add more technical skills.")

    # ---------- Education (20) ----------
    education_found = any(item in text.lower() for item in EDUCATION)

    if education_found:
        score += 20
    else:
        feedback.append("Education section missing.")

    # ---------- Experience (20) ----------
    experience_found = any(item in text.lower() for item in EXPERIENCE)

    if experience_found:
        score += 20
    else:
        feedback.append("Experience section missing.")

    # ---------- Contact (10) ----------
    if any(c in text for c in CONTACT):
        score += 10
    else:
        feedback.append("Contact information missing.")

    # ---------- Resume Length (10) ----------
    words = len(re.findall(r"\w+", text))

    if words >= 300:
        score += 10
    else:
        feedback.append("Resume is too short.")

    return score, feedback