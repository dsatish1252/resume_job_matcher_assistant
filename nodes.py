import json

from utils import llm
from prompts import *
from tools import *


def parse_json_response(response_text: str):
    """
    Parse JSON returned by the LLM.
    Handles responses wrapped in ```json ... ``` code fences.
    """
    text = response_text.strip()

    # Remove markdown code fences if present
    if text.startswith("```"):
        lines = text.splitlines()

        # Remove first line (``` or ```json)
        if lines:
            lines = lines[1:]

        # Remove last ```
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]

        text = "\n".join(lines)

    return json.loads(text)


def input_validator_node(state):

    missing = []

    if not state["resume_text"].strip():
        missing.append("Resume")

    if not state["job_description"].strip():
        missing.append("Job Description")

    state["resume_available"] = len(state["resume_text"].strip()) > 0
    state["jd_available"] = len(state["job_description"].strip()) > 0
    state["missing_information"] = missing

    return state


def resume_parser_node(state):

    prompt = RESUME_PARSER_PROMPT.format(
        resume=state["resume_text"]
    )

    response = llm.invoke(prompt)

    state["parsed_resume"] = parse_json_response(response.content[0]['text'])

    return state


def jd_parser_node(state):

    prompt = JD_PARSER_PROMPT.format(
        jd=state["job_description"]
    )

    response = llm.invoke(prompt)

    state["parsed_jd"] = parse_json_response(response.content[0]['text'])

    return state


def skill_matching_node(state):

    resume_skills = state["parsed_resume"]["core_skills"]

    required_skills = state["parsed_jd"]["required_skills"]

    matched, partial, missing = match_skills(
        resume_skills,
        required_skills
    )

    state["matched_skills"] = matched
    state["partially_matched_skills"] = partial
    state["missing_skills"] = missing

    return state


def gap_analysis_node(state):

    prompt = GAP_ANALYSIS_PROMPT.format(
        missing_skills=state["missing_skills"]
    )

    response = llm.invoke(prompt)

    state["gap_analysis"] = response.content[0]['text']

    return state


def fit_score_node(state):

    score = calculate_fit_score(
        state["matched_skills"],
        state["missing_skills"],
        state["parsed_jd"]["required_skills"]
    )

    state["fit_score"] = score

    state["fit_level"] = get_fit_level(score)

    return state


def resume_improvement_node(state):

    prompt = RESUME_IMPROVEMENT_PROMPT.format(
        resume=state["resume_text"],
        missing_skills=state["missing_skills"]
    )

    response = llm.invoke(prompt)

    state["resume_improvement_suggestions"] = response.content[0]['text']

    return state


def cover_letter_node(state):

    prompt = COVER_LETTER_PROMPT.format(
        resume=state["resume_text"],
        jd=state["job_description"]
    )

    response = llm.invoke(prompt)

    state["cover_letter"] = response.content[0]['text']

    return state


def learning_roadmap_node(state):

    roadmap = generate_learning_plan(
        state["missing_skills"]
    )

    state["learning_roadmap"] = roadmap

    return state


def final_recommendation_node(state):

    prompt = FINAL_RECOMMENDATION_PROMPT.format(
        matched=state["matched_skills"],
        missing=state["missing_skills"],
        score=state["fit_score"],
        gap=state["gap_analysis"]
    )

    response = llm.invoke(prompt)

    state["final_recommendation"] = response.content[0]['text']

    return state