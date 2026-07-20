import re

# ==========================================================
# Resume Sections
# ==========================================================

EDUCATION = [
    "education",
    "b.tech",
    "b.e",
    "bca",
    "mca",
    "m.tech",
    "msc",
    "bsc",
    "phd",
    "college",
    "university",
    "cgpa",
    "gpa",
    "bachelor",
    "master",
]

EXPERIENCE = [
    "experience",
    "intern",
    "internship",
    "developer",
    "engineer",
    "analyst",
    "software engineer",
    "data scientist",
    "business analyst",
]

PROJECTS = [
    "project",
    "projects",
]

CERTIFICATIONS = [
    "certification",
    "certifications",
    "certificate",
]

CONTACT = [
    "@",
    "+91",
    "linkedin",
    "github",
]

ACTION_VERBS = [
    "developed",
    "designed",
    "built",
    "implemented",
    "created",
    "optimized",
    "analyzed",
    "managed",
    "improved",
    "integrated",
]

# ==========================================================
# ATS Score Calculator
# ==========================================================

def calculate_ats_score(text, skills):

    text = text.lower()

    score = 0
    feedback = []

    breakdown = {
        "Technical Skills": 0,
        "Education": 0,
        "Experience": 0,
        "Projects": 0,
        "Certifications": 0,
        "Contact": 0,
        "Action Verbs": 0,
        "Resume Length": 0,
    }

    # ------------------------------------------------------
    # Technical Skills (30)
    # ------------------------------------------------------

    skill_score = min(len(skills) * 3, 30)

    breakdown["Technical Skills"] = skill_score

    score += skill_score

    if skill_score < 20:
        feedback.append("Add more relevant technical skills.")

    # ------------------------------------------------------
    # Education (15)
    # ------------------------------------------------------

    if any(word in text for word in EDUCATION):
        breakdown["Education"] = 15
        score += 15
    else:
        feedback.append("Education section missing.")

    # ------------------------------------------------------
    # Experience (15)
    # ------------------------------------------------------

    if any(word in text for word in EXPERIENCE):
        breakdown["Experience"] = 15
        score += 15
    else:
        feedback.append("Experience section missing.")

    # ------------------------------------------------------
    # Projects (10)
    # ------------------------------------------------------

    if any(word in text for word in PROJECTS):
        breakdown["Projects"] = 10
        score += 10
    else:
        feedback.append("Add at least one project.")

    # ------------------------------------------------------
    # Certifications (5)
    # ------------------------------------------------------

    if any(word in text for word in CERTIFICATIONS):
        breakdown["Certifications"] = 5
        score += 5
    else:
        feedback.append("Consider adding certifications.")

    # ------------------------------------------------------
    # Contact (10)
    # ------------------------------------------------------

    if any(word in text for word in CONTACT):
        breakdown["Contact"] = 10
        score += 10
    else:
        feedback.append("Contact information missing.")

    # ------------------------------------------------------
    # Action Verbs (5)
    # ------------------------------------------------------

    verb_count = sum(
        1 for verb in ACTION_VERBS
        if verb in text
    )

    if verb_count >= 5:
        breakdown["Action Verbs"] = 5
        score += 5
    else:
        feedback.append("Use stronger action verbs.")

    # ------------------------------------------------------
    # Resume Length (10)
    # ------------------------------------------------------

    words = len(re.findall(r"\w+", text))

    if 300 <= words <= 900:
        breakdown["Resume Length"] = 10
        score += 10

    elif words >= 200:
        breakdown["Resume Length"] = 7
        score += 7
        feedback.append("Resume could be more detailed.")

    else:
        feedback.append("Resume is too short.")

    score = min(score, 100)

    return score, feedback, breakdown