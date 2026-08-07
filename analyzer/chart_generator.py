import os
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image

matplotlib.use("Agg")

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
# Skill Match Chart
# ==========================================================

def create_skill_pie_chart(matched_count, missing_count):

    labels = ["Matched", "Missing"]
    values = [matched_count, missing_count]

    # Prevent matplotlib crash if both are zero
    if sum(values) == 0:
        values = [1, 1]

    # Professional dark-dashboard chart
    fig, ax = plt.subplots(figsize=(8, 4.8))

    fig.patch.set_facecolor("#111827")
    ax.set_facecolor("#111827")

    bars = ax.barh(
        labels,
        values,
        height=0.45,
        color=["#22C55E", "#F59E0B"]
    )

    max_value = max(values)

    ax.set_xlim(0, max_value + max(2, max_value * 0.15))

    ax.set_xlabel(
        "Number of Skills",
        color="#CBD5E1",
        fontsize=10
    )

    ax.set_title(
        "Skill Match Analysis",
        fontsize=16,
        fontweight="bold",
        color="#F8FAFC",
        pad=15
    )

    # Grid
    ax.xaxis.grid(
        True,
        linestyle="--",
        alpha=0.15,
        color="#94A3B8"
    )

    ax.set_axisbelow(True)

    # Remove unnecessary borders
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Axis text
    ax.tick_params(
        axis="x",
        colors="#94A3B8",
        labelsize=9
    )

    ax.tick_params(
        axis="y",
        colors="#E2E8F0",
        labelsize=11
    )

    # Show values
    for bar, value in zip(bars, values):

        ax.text(
            value + max(0.2, max_value * 0.02),
            bar.get_y() + bar.get_height() / 2,
            str(value),
            va="center",
            fontsize=11,
            fontweight="bold",
            color="#F8FAFC"
        )

    plt.tight_layout()

    chart_path = os.path.join(
        CHART_DIR,
        "skill_pie_chart.png"
    )

    plt.savefig(
        chart_path,
        dpi=150,
        bbox_inches="tight",
        facecolor=fig.get_facecolor()
    )

    plt.close(fig)
    return chart_path


# ==========================================================
# ATS Breakdown Horizontal Bar Chart
# ==========================================================

def create_ats_bar_chart(breakdown):

    labels = list(breakdown.keys())
    values = list(breakdown.values())

    # Reverse so highest/first category appears at top
    labels = labels[::-1]
    values = values[::-1]

    fig, ax = plt.subplots(figsize=(10, 6))

    fig.patch.set_facecolor("#111827")
    ax.set_facecolor("#111827")

    bars = ax.barh(
        labels,
        values,
        height=0.55,
        color="#3B82F6"
    )

    max_value = max(values) if values else 1

    ax.set_xlim(
        0,
        max_value + max(3, max_value * 0.15)
    )

    ax.set_xlabel(
        "Points",
        color="#CBD5E1",
        fontsize=10
    )

    ax.set_title(
        "Resume Quality Breakdown",
        fontsize=16,
        fontweight="bold",
        color="#F8FAFC",
        pad=15
    )

    # Grid
    ax.xaxis.grid(
        True,
        linestyle="--",
        alpha=0.15,
        color="#94A3B8"
    )

    ax.set_axisbelow(True)

    # Remove borders
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Axis styling
    ax.tick_params(
        axis="x",
        colors="#94A3B8",
        labelsize=9
    )

    ax.tick_params(
        axis="y",
        colors="#E2E8F0",
        labelsize=10
    )

    # Show values
    for bar, value in zip(bars, values):

        ax.text(
            value + max(0.2, max_value * 0.02),
            bar.get_y() + bar.get_height() / 2,
            str(int(value)),
            va="center",
            fontsize=10,
            fontweight="bold",
            color="#F8FAFC"
        )

    plt.tight_layout()

    chart_path = os.path.join(
        CHART_DIR,
        "ats_breakdown_chart.png"
    )

    fig.canvas.draw()

    plt.savefig(
        chart_path,
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor()
    )

    plt.close(fig)
    return chart_path