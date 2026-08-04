from analyzer.interview_feedback import evaluate_answer

response = evaluate_answer(
    question="Tell me about your experience with Python.",
    answer="""
I have used Python for data analysis, machine learning,
and building AI projects like a Resume Analyzer AI.
I have experience with Pandas, NumPy,
Scikit-learn, and FastAPI.
"""
)

print(response)