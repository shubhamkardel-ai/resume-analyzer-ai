import random

QUESTION_BANK = {
    "python": [
        "Explain your experience with Python.",
        "What are Python decorators?",
        "How do you handle exceptions in Python?",
        "What is the difference between a list and a tuple?",
        "Describe your favorite Python project."
    ],

    "machine learning": [
        "Explain the machine learning lifecycle.",
        "What is overfitting?",
        "How do you evaluate a machine learning model?",
        "Which algorithms have you used?",
        "Describe a machine learning project you built."
    ],

    "scikit-learn": [
        "Which Scikit-learn models have you used?",
        "How do you split training and testing data?",
        "What is GridSearchCV?",
        "How do you preprocess data using Scikit-learn?",
        "Describe a project built with Scikit-learn."
    ],

    "pandas": [
        "Why is Pandas important in Data Science?",
        "How do you handle missing values?",
        "Explain groupby().",
        "What is the difference between loc and iloc?",
        "Describe a project using Pandas."
    ],

    "numpy": [
        "Why is NumPy faster than Python lists?",
        "Explain NumPy arrays.",
        "What are broadcasting operations?",
        "Describe vectorization.",
        "Where have you used NumPy?"
    ],

    "sql": [
        "Explain SQL joins.",
        "Difference between WHERE and HAVING?",
        "What are primary and foreign keys?",
        "Write a query to find duplicate rows.",
        "Describe your SQL experience."
    ],

    "fastapi": [
        "Why use FastAPI?",
        "Difference between Flask and FastAPI?",
        "Explain API routing.",
        "How do you deploy FastAPI?",
        "Describe a FastAPI project."
    ],

    "git": [
        "Explain Git branching.",
        "Difference between merge and rebase?",
        "How do you resolve merge conflicts?",
        "Describe your Git workflow.",
        "Why is version control important?"
    ],

    "github": [
        "How do you collaborate using GitHub?",
        "Explain Pull Requests.",
        "What is GitHub Actions?",
        "Describe your GitHub portfolio.",
        "How do you manage repositories?"
    ]
}


def get_questions(skill):
    """
    Returns 3 random interview questions
    for the given skill.
    """

    skill = skill.lower()

    if skill not in QUESTION_BANK:
        return [
            f"Explain your experience with {skill.title()}."
        ]

    return random.sample(
        QUESTION_BANK[skill],
        min(3, len(QUESTION_BANK[skill]))
    )