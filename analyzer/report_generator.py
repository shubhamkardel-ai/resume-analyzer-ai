from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    ats_score,
    job_match,
    matched_skills,
    missing_skills,
    breakdown,
    ai_feedback,
    optimized_resume,
):
    """
    Generates a Resume Analysis PDF report.

    Returns
    -------
    str
        Path to generated PDF.
    """

    pdf_path = "resume_analysis_report.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(pdf_path)

    elements = []

    elements.append(Paragraph("<b>Resume Analysis Report</b>", styles["Title"]))

    elements.append(Paragraph(f"<b>ATS Score:</b> {ats_score}/100", styles["BodyText"]))
    elements.append(Paragraph(f"<b>Job Match:</b> {job_match}%", styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"]))
    elements.append(Paragraph(matched_skills.replace("\n", "<br/>"), styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))
    elements.append(Paragraph(missing_skills.replace("\n", "<br/>"), styles["BodyText"]))

    elements.append(Paragraph("<br/><b>ATS Breakdown</b>", styles["Heading2"]))
    elements.append(Paragraph(breakdown.replace("\n", "<br/>"), styles["BodyText"]))

    elements.append(Paragraph("<br/><b>AI Career Coach</b>", styles["Heading2"]))
    elements.append(Paragraph(ai_feedback.replace("\n", "<br/>"), styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Optimized Resume</b>", styles["Heading2"]))
    elements.append(
        Paragraph(
            optimized_resume.replace("\n", "<br/>"),
            styles["BodyText"],
        )
    )

    doc.build(elements)

    return pdf_path