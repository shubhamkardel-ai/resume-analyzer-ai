import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def generate_report(
    ats_score,
    job_match,
    matched_skills,
    missing_skills,
    ats_breakdown,
    ai_feedback,
    optimized_resume,
):
    """
    Generate a professional PDF report.

    Returns
    -------
    str
        Path of generated PDF.
    """

    report_path = os.path.join(
        "assets",
        "resume_analysis_report.pdf"
    )

    os.makedirs("assets", exist_ok=True)

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(report_path)

    story = []

    story.append(
        Paragraph(
            "<b>Resume Analysis Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}/100",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Job Match:</b> {job_match}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Matched Skills</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            matched_skills.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Missing Skills</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            missing_skills.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>ATS Breakdown</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            ats_breakdown.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>AI Career Coach</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            ai_feedback.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>AI Resume Optimizer</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            optimized_resume.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return report_path