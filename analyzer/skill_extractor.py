import re

# ==========================================================
# Master Skill List
# ==========================================================

SKILLS = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",

    # Data Science
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "plotly",

    # Machine Learning
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",
    "xgboost",
    "lightgbm",

    # Computer Vision
    "computer vision",
    "opencv",
    "yolo",
    "mediapipe",

    # NLP
    "nltk",
    "spacy",
    "transformers",
    "bert",

    # LLM / GenAI
    "langchain",
    "llm",
    "generative ai",
    "prompt engineering",
    "rag",
    "vector database",

    # Backend
    "fastapi",
    "flask",
    "django",
    "rest api",

    # Visualization
    "power bi",
    "tableau",
    "excel",
    "power query",
    "dax",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # DevOps
    "docker",
    "kubernetes",

    # Version Control
    "git",
    "github",

    # IDE / Tools
    "pycharm",
    "jupyter notebook",
    "google colab",
    "vscode",

    # Libraries
    "pygame",
    "streamlit",
    "gradio",
]

# ==========================================================
# Skill Aliases
# ==========================================================

ALIASES = {

    # ML
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",

    # Power BI
    "powerbi": "power bi",
    "power-bi": "power bi",

    # Excel
    "ms excel": "excel",
    "microsoft excel": "excel",

    # PyTorch
    "py torch": "pytorch",

    # OpenCV
    "opencv-python": "opencv",

    # GitHub
    "git hub": "github",

    # Jupyter
    "jupyter": "jupyter notebook",

    # Google Colab
    "colab": "google colab",

    # VS Code
    "vs code": "vscode",
    "visual studio code": "vscode",

    # GenAI
    "gen ai": "generative ai",

    # APIs
    "restful api": "rest api",
    "restful apis": "rest api",
}

# ==========================================================
# Skill Extraction
# ==========================================================

def extract_skills(text):
    """
    Extract technical skills from resume text.

    Parameters
    ----------
    text : str
        Resume text extracted from PDF.

    Returns
    -------
    list
        Sorted list of detected skills.
    """

    if not text:
        return []

    text = text.lower()

    # Normalize aliases
    for alias, original in ALIASES.items():
        text = text.replace(alias, original)

    found = set()

    # Detect skills using regex
    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found.add(skill.title())

    return sorted(found)