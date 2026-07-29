import os
import matplotlib.pyplot as plt

# ==========================================================
# Charts Folder
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CHART_DIR = os.path.join(
    BASE_DIR,
    "assets",
    "charts"
)

os.makedirs(CHART_DIR, exist_ok=True)


# ==========================================================
# Skill Pie Chart
# ==========================================================

def create_skill_pie_chart(matched_count, missing_count):

    labels = ["Matched", "Missing"]

    values = [matched_count, missing_count]

    # Prevent matplotlib crash if both are zero
    if sum(values) == 0:
        values = [1, 1]

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#4CAF50", "#F44336"],
        wedgeprops={"edgecolor": "white"}
    )

    ax.set_title(
        "Skill Match Analysis",
        fontsize=16,
        fontweight="bold"
    )

    chart_path = os.path.join(
        CHART_DIR,
        "skill_pie_chart.png"
    )

    plt.tight_layout()

    plt.savefig(
        chart_path,
        dpi=300
    )

    plt.close(fig)

    return chart_path


# ==========================================================
# ATS Breakdown Bar Chart
# ==========================================================

def create_ats_bar_chart(breakdown):

    labels = list(breakdown.keys())

    values = list(breakdown.values())

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.bar(
        labels,
        values
    )

    ax.set_ylim(0, 30)

    ax.set_title(
        "ATS Score Breakdown",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_ylabel("Points")

    plt.xticks(rotation=25)

    # Show values above bars
    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.3,
            str(int(height)),
            ha="center"
        )

    chart_path = os.path.join(
        CHART_DIR,
        "ats_breakdown_chart.png"
    )

    plt.tight_layout()

    plt.savefig(
        chart_path,
        dpi=300
    )

    plt.close(fig)

    return chart_path