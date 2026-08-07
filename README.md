# 🤖 Resume Analyzer AI

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,25:061A3A,50:0B3B60,75:007C91,100:00F7FF&height=250&section=header&text=RESUME%20ANALYZER%20AI&fontSize=52&fontColor=FFFFFF&fontAlignY=38&desc=AI-POWERED%20CAREER%20INTELLIGENCE%20PLATFORM&descAlignY=60&descSize=18&animation=fadeIn" width="100%"/>

<br>

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=20&duration=2200&pause=700&color=00F7FF&center=true&vCenter=true&width=950&lines=ANALYZE+RESUMES;MATCH+JOBS;DISCOVER+SKILL+GAPS;OPTIMIZE+APPLICATIONS;PREPARE+FOR+INTERVIEWS;BUILD+BETTER+CAREERS" />

<br><br>

<img src="https://img.shields.io/badge/PROJECT-RESUME%20ANALYZER%20AI-00F7FF?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/STATUS-COMPLETE-00FF9C?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/FOCUS-AI%20%7C%20NLP%20%7C%20ML-00F7FF?style=for-the-badge&labelColor=020617"/>
<img src="https://img.shields.io/badge/INTERFACE-GRADIO-00F7FF?style=for-the-badge&labelColor=020617"/>

</div>

---

# 📌 Overview

**Resume Analyzer AI** is an AI-powered career intelligence platform designed to analyze resumes, evaluate ATS readiness, extract technical and professional skills, compare resumes against job descriptions, identify skill gaps, generate visual analytics, provide AI-powered career feedback, optimize resumes, generate cover letters, create ATS reports, conduct AI-powered interviews, evaluate answers, and enable resume-grounded conversations.

The platform goes beyond a traditional ATS checker by combining:

**Document Processing + NLP + Skill Intelligence + ATS Evaluation + Job Matching + Visual Analytics + LLM-powered Career Intelligence**

into a unified application.

---

# 🎯 Core Objective

The objective of Resume Analyzer AI is to transform resume analysis from a simple score into **actionable career intelligence**.

The platform helps users:

- 📄 Understand their resume
- 📊 Evaluate ATS readiness
- 🧠 Discover technical skills
- 🎯 Measure job alignment
- ❌ Identify missing skills
- 💡 Receive improvement recommendations
- ✨ Optimize resume content
- 💌 Generate job-specific cover letters
- 📄 Generate ATS analysis reports
- 🎤 Practice job-focused interviews
- 🧠 Evaluate interview answers
- 💬 Chat with their resume

---

# ✨ Features

<div align="center">

| Feature | Description |
|---|---|
| 📄 PDF Resume Processing | Extract resume content from uploaded PDF documents |
| 🧠 Skill Extraction | Detect technical and professional skills |
| 📊 ATS Scoring | Calculate ATS-oriented resume readiness |
| 🎯 Job Matching | Compare resume against a target job description |
| ✅ Matched Skills | Identify skills already present |
| ❌ Missing Skills | Identify important skill gaps |
| 📋 ATS Suggestions | Generate resume improvement recommendations |
| 📈 Visual Analytics | Generate ATS and skill matching charts |
| 🤖 AI Career Coach | Provide AI-powered career insights |
| ✨ Resume Optimizer | Improve resume content and job alignment |
| 💌 Cover Letter Generator | Generate job-focused cover letters |
| 📄 ATS PDF Report | Generate downloadable resume analysis reports |
| 🎤 AI Interview Coach | Generate interview questions from resume and JD |
| 🧠 Answer Evaluation | Evaluate technical, communication and confidence scores |
| 💬 Resume Chat | Ask questions about the uploaded resume |

</div>

---

# 🧠 System Architecture

The application follows a modular architecture where each component performs a dedicated responsibility while the centralized `resume_service.py` coordinates the main resume-analysis workflow.

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=16&duration=1800&pause=500&color=00FF9C&center=true&vCenter=true&width=1000&lines=SYSTEM+INITIALIZED;%3E+INPUT%3A+RESUME+PDF;%3E+PDF_READER;%3E+SKILL_EXTRACTOR;%3E+ATS_SCORE;%3E+JD_MATCHER;%3E+CHART_GENERATOR;%3E+AI_FEEDBACK;%3E+RESUME_SERVICE;%3E+RESUME_OPTIMIZER;%3E+COVER_LETTER;%3E+ATS_REPORT;%3E+INTERVIEW_COACH;%3E+ANSWER_EVALUATION;%3E+RESUME_CHAT;%3E+OUTPUT%3A+CAREER+INTELLIGENCE" />

</div>

---

# 🧩 Core Modules

| Module | Responsibility |
|---|---|
| 📄 `pdf_reader.py` | Extracts text from uploaded PDF resumes |
| 🧠 `skill_extractor.py` | Detects technical and professional skills |
| 📊 `ats_score.py` | Calculates ATS-oriented resume score |
| 🎯 `jd_matcher.py` | Matches resume skills against job requirements |
| 🤖 `ai_feedback.py` | Generates AI-powered career feedback |
| 📈 `chart_generator.py` | Generates ATS and skill visualizations |
| 🔄 `resume_service.py` | Coordinates the complete resume analysis workflow |
| 📋 `suggestions.py` | Generates ATS improvement suggestions |
| 🖥️ `app.py` | Runs the Gradio application |

---

# 🔄 Analysis Workflow

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=17&duration=1800&pause=600&color=00F7FF&center=true&vCenter=true&width=1000&lines=%5B01%5D+UPLOAD+RESUME;%5B02%5D+EXTRACT+PDF+CONTENT;%5B03%5D+DETECT+SKILLS;%5B04%5D+CALCULATE+ATS+SCORE;%5B05%5D+ANALYZE+JOB+DESCRIPTION;%5B06%5D+MATCH+RESUME+WITH+JOB;%5B07%5D+GENERATE+VISUAL+ANALYTICS;%5B08%5D+GENERATE+AI+INSIGHTS;%5B09%5D+OPTIMIZE+RESUME;%5B10%5D+GENERATE+COVER+LETTER;%5B11%5D+CREATE+ATS+REPORT;%5B12%5D+START+AI+INTERVIEW;%5B13%5D+EVALUATE+ANSWER;%5B14%5D+CHAT+WITH+RESUME" />

</div>

---

# 🤖 AI Career Coach

The **AI Career Coach** uses the results of the resume analysis pipeline to provide actionable career feedback.

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=17&duration=2000&pause=600&color=00F7FF&center=true&vCenter=true&width=1000&lines=RESUME+CONTENT+%2B+ATS+SCORE+%2B+SKILLS+%2B+JOB+MATCH;%3E%3E+AI+CAREER+COACH;%3E%3E+RESUME+STRENGTHS;%3E%3E+RESUME+WEAKNESSES;%3E%3E+MISSING+SKILLS;%3E%3E+IMPROVEMENT+AREAS;%3E%3E+JOB+ALIGNMENT;%3E%3E+ACTIONABLE+RECOMMENDATIONS" />

</div>

The AI Career Coach helps users understand:

- Resume strengths
- Resume weaknesses
- Missing technical skills
- ATS improvement opportunities
- Job alignment
- Career improvement priorities
- Actionable recommendations

---

# ✨ AI Resume Optimizer

The **AI Resume Optimizer** analyzes the existing resume and provides improvement-oriented recommendations.

It focuses on:

- Resume content improvement
- ATS keyword alignment
- Skill presentation
- Project descriptions
- Professional wording
- Resume structure
- Job-specific improvements
- Stronger career positioning

The goal is to transform an existing resume into a more targeted and ATS-friendly version.

---

# 💌 AI Cover Letter Generator

The **AI Cover Letter Generator** creates a job-focused cover letter using resume information and target job requirements.

It can consider:

- Candidate skills
- Experience
- Projects
- Target role
- Job requirements
- Relevant technical strengths

This extends the workflow from:

**Resume Analysis → Job Matching → Application Preparation**

---

# 📄 ATS PDF Report

The platform generates an ATS-focused PDF report containing important analysis results.

The report can include:

- ATS score
- ATS breakdown
- Resume skills
- Job skills
- Matched skills
- Missing skills
- Job match score
- Improvement suggestions
- Career insights

This provides a portable version of the analysis for later review.

---

# 🎤 AI Interview Coach

The **AI Interview Coach** extends the platform beyond resume optimization.

It prepares users for interviews using their resume and target job description.

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=16&duration=1800&pause=600&color=00FF9C&center=true&vCenter=true&width=1000&lines=RESUME+%2B+JOB+DESCRIPTION;%3E+INTERVIEW+CONTEXT;%3E+QUESTION+GENERATION;%3E+CANDIDATE+ANSWER;%3E+ANSWER+EVALUATION;%3E+TECHNICAL+SCORE;%3E+COMMUNICATION+SCORE;%3E+CONFIDENCE+SCORE;%3E+FEEDBACK;%3E+NEXT+QUESTION" />

</div>

### Interview Capabilities

- 🎯 Generate interview questions
- 📄 Use resume context
- 💼 Use job-description context
- 🧠 Evaluate candidate answers
- 💻 Technical evaluation
- 💬 Communication evaluation
- 🎤 Confidence evaluation
- 🔄 Continue to the next question

---

# 💬 Resume Chat

Resume Chat allows users to interact directly with their uploaded resume.

### Example Questions

```text
What are my technical skills?

What projects have I worked on?

What is my Data Science experience?

What machine learning technologies do I know?

What are my strongest projects?

What skills are mentioned in my resume?
