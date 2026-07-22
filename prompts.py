INPUT_VALIDATOR_PROMPT = """
You are an Input Validation Agent.

Check whether the following inputs are present.

Resume:
{resume}

Job Description:
{jd}

Return ONLY JSON.

Example:

{{
    "resume_available": true,
    "jd_available": true,
    "missing_information": []
}}
"""


RESUME_PARSER_PROMPT = """
You are an expert Resume Parsing Agent.

Extract the following information from the resume.

Resume

{resume}

Return ONLY JSON.

{{
  "candidate_name":"",
  "total_experience":"",
  "core_skills":[],
  "projects":[],
  "certifications":[]
}}

Do not explain anything.
Return valid JSON only.
"""


JD_PARSER_PROMPT = """
You are a Job Description Parsing Agent.

Read the Job Description carefully.

Job Description

{jd}

Extract

1 Job Title

2 Required Skills

3 Preferred Skills

4 Experience Required

Return ONLY JSON.

Example

{{
 "job_title":"",
 "required_skills":[],
 "preferred_skills":[],
 "experience_required":""
}}
"""


SKILL_MATCH_PROMPT = """
You are a Skill Matching Agent.

Resume Skills

{resume_skills}

Required Skills

{required_skills}

Preferred Skills

{preferred_skills}

Compare the resume skills against the required and preferred skills.
Use semantic understanding, synonyms, and role context rather than exact string matching.
Treat skills as matched when the resume demonstrates equivalent or closely related capabilities.
If a resume skill is related but not directly equivalent, classify it as partially matched.
If the resume does not show the required capability, classify it as missing.

Return JSON only.

{{
 "matched_skills":[],
 "partially_matched_skills":[],
 "missing_skills":[]
}}
"""


SKILL_EXTRACTION_PROMPT = """
You are an expert resume skill extraction agent.

Extract all skills, technologies, tools, certifications, and qualifications mentioned in the text below.

Text:
{text}

Return ONLY a JSON array of strings.
For example:
["Python", "Machine Learning", "SAP BTP"]

Do not add any explanation, markdown, or extra text.
"""


GAP_ANALYSIS_PROMPT = """
You are a Career Coach.

The candidate has the following missing skills.

{missing_skills}

Explain

1 Why these skills matter

2 Which are critical

3 How the candidate can improve

Keep the answer within 200 words.
"""


RESUME_IMPROVEMENT_PROMPT = """
You are an expert Resume Reviewer.

Candidate Resume

{resume}

Missing Skills

{missing_skills}

Suggest

• Resume improvements

• Keywords to add

• Projects to mention

• Certifications to add

Keep the response concise.
"""


COVER_LETTER_PROMPT = """
You are an HR recruiter.

Generate a professional cover letter.

Resume

{resume}

Job Description

{jd}

Keep it under 250 words.

Professional tone.

Return only the cover letter.
"""


LEARNING_ROADMAP_PROMPT = """
You are an AI Career Coach.

Missing Skills

{missing_skills}

Generate a learning roadmap.

For each skill include

• What to learn

• Beginner resources

• Small project

• Resume tip

Use bullet points.
"""


FINAL_RECOMMENDATION_PROMPT = """
You are a Senior Hiring Manager.

Candidate Information

Matched Skills

{matched}

Missing Skills

{missing}

Fit Score

{score}

Gap Analysis

{gap}

Give

1 Final Recommendation

2 Should Apply?

3 Confidence Level

4 Short Summary

Professional tone.
"""


