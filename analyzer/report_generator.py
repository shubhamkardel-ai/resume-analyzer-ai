import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


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

    report_dir = os.path.join(
        os.getcwd(),
        "assets"
    )

    os.makedirs(report_dir, exist_ok=True)

    report_path = os.path.join(
        report_dir,
        "resume_analysis_report.pdf"
    )

    os.makedirs("assets", exist_ok=True)

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        leading=26,
        spaceAfter=12,
    )

    section_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.HexColor("#0B3B60"),
    )

    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15,
        spaceAfter=6,
    )

    score_style = ParagraphStyle(
        "Score",
        parent=styles["BodyText"],
        alignment=TA_CENTER,
        fontSize=14,
        leading=18,
        spaceAfter=8,
    )

    doc = SimpleDocTemplate(
        report_path,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    story = []

    story.append(
        Paragraph(
            "Resume Analysis Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            "AI-Powered ATS Screening & Career Analysis",
            score_style
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}/100",
            score_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Job Match:</b> {job_match}%",
            score_style
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