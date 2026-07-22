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

Compare them.

Return JSON only.

{{
 "matched_skills":[],
 "partially_matched_skills":[],
 "missing_skills":[]
}}
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


