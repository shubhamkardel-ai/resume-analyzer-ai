import re


def extract_section(text, section_name):
    """
    Extract a resume section using heading names.
    """

    upper_text = text.upper()
    section_name = section_name.upper()

    headings = [
        "EDUCATION",
        "EXPERIENCE",
        "PROJECTS",
        "SKILLS",
        "CERTIFICATIONS"
    ]

    start = upper_text.find(section_name)

    if start == -1:
        return f"Section '{section_name}' not found."

    start += len(section_name)

    end = len(text)

    for heading in headings:
        if heading == section_name:
            continue

        pos = upper_text.find(heading, start)

        if pos != -1 and pos < end:
            end = pos

    return text[start:end].strip()