from typing import TypedDict, List, Optional


class JobMatchState(TypedDict):
    # Inputs
    resume_text: str
    job_description: str

    # Validation
    resume_available: bool
    jd_available: bool
    missing_information: List[str]

    # Parsed Information
    parsed_resume: Optional[dict]
    parsed_jd: Optional[dict]

    # Skill Matching
    matched_skills: List[str]
    partially_matched_skills: List[str]
    missing_skills: List[str]

    # Analysis
    gap_analysis: Optional[str]

    # Fit Score
    fit_score: Optional[int]
    fit_level: Optional[str]

    # Routing Outputs
    resume_improvement_suggestions: Optional[str]
    learning_roadmap: Optional[str]
    cover_letter: Optional[str]

    # Final Output
    final_recommendation: Optional[str]