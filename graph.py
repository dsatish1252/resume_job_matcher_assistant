from langgraph.graph import StateGraph, END

from state import JobMatchState

from nodes import (
    input_validator_node,
    resume_parser_node,
    jd_parser_node,
    skill_matching_node,
    gap_analysis_node,
    fit_score_node,
    resume_improvement_node,
    learning_roadmap_node,
    cover_letter_node,
    final_recommendation_node,
)

workflow = StateGraph(JobMatchState)

workflow.add_node("validator", input_validator_node)
workflow.add_node("resume_parser", resume_parser_node)
workflow.add_node("jd_parser", jd_parser_node)
workflow.add_node("skill_matching", skill_matching_node)
workflow.add_node("gap_analysis", gap_analysis_node)
workflow.add_node("fit_score", fit_score_node)
workflow.add_node("resume_improvement", resume_improvement_node)
workflow.add_node("learning_roadmap", learning_roadmap_node)
workflow.add_node("cover_letter", cover_letter_node)
workflow.add_node("final_recommendation", final_recommendation_node)

workflow.set_entry_point("validator")

workflow.add_edge("validator", "resume_parser")
workflow.add_edge("resume_parser", "jd_parser")
workflow.add_edge("jd_parser", "skill_matching")
workflow.add_edge("skill_matching", "gap_analysis")
workflow.add_edge("gap_analysis", "fit_score")


def route_based_on_score(state):
    score = state["fit_score"]

    if score >= 80:
        return "strong"

    elif score >= 60:
        return "medium"

    else:
        return "weak"


workflow.add_conditional_edges(
    "fit_score",
    route_based_on_score,
    {
        "strong": "cover_letter",
        "medium": "resume_improvement",
        "weak": "learning_roadmap",
    },
)

workflow.add_edge(
    "cover_letter",
    "final_recommendation",
)

workflow.add_edge(
    "resume_improvement",
    "final_recommendation",
)

workflow.add_edge(
    "learning_roadmap",
    "final_recommendation",
)

workflow.add_edge(
    "final_recommendation",
    END,
)

graph = workflow.compile()
