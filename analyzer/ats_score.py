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
# ATS Score Calculator v2
# ==========================================================

def calculate_ats_score(text, skills):

    text = text.lower()

    score = 0
    feedback = []

    breakdown = {
        "Technical Skills": 0,
        "Job Relevance": 0,
        "Projects": 0,
        "Experience": 0,
        "Education": 0,
        "Resume Structure": 0,
        "Action Verbs": 0,
        "Contact": 0,
    }

    # ======================================================
    # 1. Technical Skills — 30 Points
    # ======================================================

    skill_score = min(len(skills) * 2, 30)

    breakdown["Technical Skills"] = skill_score
    score += skill_score

    if skill_score < 15:
        feedback.append(
            "Add more relevant technical skills."
        )


    # ======================================================
    # 2. Job Relevance — 25 Points
    # ======================================================
    #
    # This category measures whether the resume contains
    # meaningful technical/job-related keywords.
    #
    # It is intentionally separate from raw skill count.
    # ======================================================

    relevance_keywords = [
        "machine learning",
        "data science",
        "artificial intelligence",
        "deep learning",
        "python",
        "sql",
        "scikit-learn",
        "pandas",
        "numpy",
        "model",
        "prediction",
        "data analysis",
        "feature engineering",
        "computer vision",
        "generative ai",
        "llm",
        "nlp",
    ]

    matched_relevance = sum(
        1 for keyword in relevance_keywords
        if keyword in text
    )

    relevance_score = min(
        int((matched_relevance / len(relevance_keywords)) * 25),
        25
    )

    breakdown["Job Relevance"] = relevance_score
    score += relevance_score

    if relevance_score < 12:
        feedback.append(
            "Tailor your resume more closely to the target job."
        )


    # ======================================================
    # 3. Projects — 15 Points
    # ======================================================

    project_count = len(
        re.findall(r"\bprojects?\b", text)
    )

    if project_count >= 2:
        project_score = 15

    elif project_count == 1:
        project_score = 10

    else:
        project_score = 0
        feedback.append(
            "Add relevant technical projects."
        )

    breakdown["Projects"] = project_score
    score += project_score


    # ======================================================
    # 4. Experience — 10 Points
    # ======================================================

    experience_matches = sum(
        1 for word in EXPERIENCE
        if word in text
    )

    if experience_matches >= 3:
        experience_score = 10

    elif experience_matches >= 1:
        experience_score = 8

    else:
        experience_score = 0
        feedback.append(
            "Add relevant professional experience."
        )

    breakdown["Experience"] = experience_score
    score += experience_score


    # ======================================================
    # 5. Education — 5 Points
    # ======================================================

    if any(word in text for word in EDUCATION):

        breakdown["Education"] = 5
        score += 5

    else:

        feedback.append(
            "Education section missing."
        )


    # ======================================================
    # 6. Resume Structure — 5 Points
    # ======================================================

    structure_sections = [
        "education",
        "experience",
        "projects",
        "skills",
        "certifications",
    ]

    structure_count = sum(
        1
        for section in structure_sections
        if section in text
    )

    structure_score = min(
        structure_count,
        5
    )

    breakdown["Resume Structure"] = structure_score
    score += structure_score

    if structure_score < 4:
        feedback.append(
            "Improve resume section structure."
        )


    # ======================================================
    # 7. Action Verbs — 5 Points
    # ======================================================

    verb_count = sum(
        1
        for verb in ACTION_VERBS
        if verb in text
    )

    action_score = min(
        verb_count,
        5
    )

    breakdown["Action Verbs"] = action_score
    score += action_score

    if action_score < 3:
        feedback.append(
            "Use stronger action verbs in project and experience descriptions."
        )


    # ======================================================
    # 8. Contact — 5 Points
    # ======================================================

    contact_matches = sum(
        1
        for item in CONTACT
        if item in text
    )

    contact_score = min(
        contact_matches,
        5
    )

    breakdown["Contact"] = contact_score
    score += contact_score

    if contact_score < 3:
        feedback.append(
            "Complete your professional contact information."
        )


    # ======================================================
    # Final Score
    # ======================================================

    score = min(
        max(score, 0),
        100
    )

    # Remove duplicate feedback
    feedback = list(dict.fromkeys(feedback))

    # If everything is excellent
    if not feedback:
        feedback.append(
            "Excellent resume structure and ATS optimization."
        )

    return score, feedback, breakdown