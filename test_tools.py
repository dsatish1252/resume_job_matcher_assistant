from tools import *

resume = """
Python
SAP BTP
SAP AI Core
LangGraph
"""

jd = """
SAP BTP
SAP AI Core
SAP Joule
Python
"""

resume_skills = extract_skills(resume)
jd_skills = extract_skills(jd)

matched, partial, missing = match_skills(
    resume_skills,
    jd_skills,
)

score = calculate_fit_score(
    matched,
    missing,
    jd_skills,
)

print("Resume Skills:", resume_skills)
print("JD Skills:", jd_skills)
print("Matched:", matched)
print("Missing:", missing)
print("Score:", score)
print(get_fit_level(score))
print(generate_learning_plan(missing))