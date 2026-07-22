import re
from pypdf import PdfReader


# --------------------------------------------------------
# Skill Normalizer
# --------------------------------------------------------

SKILL_MAP = {
    "sap gen ai": "SAP Generative AI Hub",
    "sap generative ai": "SAP Generative AI Hub",
    "gen ai": "Generative AI",
    "genai": "Generative AI",
    "btp": "SAP BTP",
    "sap btp": "SAP BTP",
    "cpi": "SAP Integration Suite",
    "integration suite": "SAP Integration Suite",
    "hana": "SAP HANA Cloud",
    "hana cloud": "SAP HANA Cloud",
    "ai core": "SAP AI Core",
    "sap ai core": "SAP AI Core",
    "joule": "SAP Joule",
}


def normalize_skill(skill: str) -> str:
    skill = skill.strip().lower()

    if skill in SKILL_MAP:
        return SKILL_MAP[skill]

    return skill.title()


# --------------------------------------------------------
# PDF Reader
# --------------------------------------------------------

def extract_text_from_pdf(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# --------------------------------------------------------
# Text Cleaner
# --------------------------------------------------------

def clean_text(text: str):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------------------------
# Extract Skills
# --------------------------------------------------------

KNOWN_SKILLS = [
    "SAP BTP",
    "SAP AI Core",
    "SAP Generative AI Hub",
    "SAP Joule",
    "SAP HANA Cloud",
    "SAP Integration Suite",
    "CAP",
    "ABAP",
    "ABAP Cloud",
    "RAP",
    "Python",
    "LangChain",
    "LangGraph",
    "RAG",
    "GraphRAG",
    "Vector DB",
    "Prompt Engineering",
    "Agentic AI",
    "SAP Build Process Automation",
]


def extract_skills(text):

    text = text.lower()

    skills = []

    for skill in KNOWN_SKILLS:

        if skill.lower() in text:
            skills.append(skill)

    return sorted(list(set(skills)))


# --------------------------------------------------------
# Match Skills
# --------------------------------------------------------

def match_skills(resume_skills, jd_skills):

    matched = []

    missing = []

    partial = []

    resume_lower = [x.lower() for x in resume_skills]

    for skill in jd_skills:

        if skill.lower() in resume_lower:

            matched.append(skill)

        elif any(skill.lower() in r for r in resume_lower):

            partial.append(skill)

        else:

            missing.append(skill)

    return matched, partial, missing


# --------------------------------------------------------
# Fit Score
# --------------------------------------------------------

def calculate_fit_score(
        matched_skills,
        missing_skills,
        required_skills,
):

    if len(required_skills) == 0:
        return 0

    score = len(matched_skills) / len(required_skills)

    score *= 100

    penalty = len(missing_skills) * 4

    score -= penalty

    score = max(0, min(100, int(score)))

    return score


# --------------------------------------------------------
# Fit Level
# --------------------------------------------------------

def get_fit_level(score):

    if score >= 80:
        return "Strong Fit"

    elif score >= 60:
        return "Medium Fit"

    elif score >= 40:
        return "Weak Fit"

    return "Poor Fit"


# --------------------------------------------------------
# Learning Roadmap
# --------------------------------------------------------

def generate_learning_plan(missing_skills):

    if len(missing_skills) == 0:

        return "No learning roadmap required."

    plan = "Learning Roadmap\n\n"

    for i, skill in enumerate(missing_skills, start=1):

        plan += f"{i}. Learn {skill}\n"

        plan += f"   - Study fundamentals\n"

        plan += f"   - Build one project\n"

        plan += f"   - Add it to your resume\n\n"

    return plan