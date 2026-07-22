import streamlit as st

from graph import graph
from tools import extract_text_from_pdf

st.set_page_config(
    page_title="Resume Job Match Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Resume Job Match Assistant")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=300
)

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Upload a Resume")
        st.stop()

    if job_description.strip() == "":
        st.error("Enter Job Description")
        st.stop()

    resume_text = extract_text_from_pdf(uploaded_resume)

    initial_state = {

        "resume_text": resume_text,
        "job_description": job_description,

        "resume_available": False,
        "jd_available": False,
        "missing_information": [],

        "parsed_resume": None,
        "parsed_jd": None,

        "matched_skills": [],
        "partially_matched_skills": [],
        "missing_skills": [],

        "gap_analysis": None,

        "fit_score": None,
        "fit_level": None,

        "resume_improvement_suggestions": None,
        "learning_roadmap": None,
        "cover_letter": None,

        "final_recommendation": None,
    }

    with st.spinner("Analyzing Resume..."):

        result = graph.invoke(initial_state)

    st.success("Analysis Completed")

    st.metric(
        "Fit Score",
        f"{result['fit_score']}%"
    )

    st.write(result["fit_level"])

    if result.get("parsed_resume") and result["parsed_resume"].get("core_skills"):
        st.header("Resume Skills")
        st.write(result["parsed_resume"]["core_skills"])

    st.header("Matched Skills")
    st.write(result["matched_skills"])

    st.header("Missing Skills")
    st.write(result["missing_skills"])

    st.header("Gap Analysis")
    st.write(result["gap_analysis"])

    if result["cover_letter"]:
        st.header("Cover Letter")
        st.write(result["cover_letter"])

    if result["resume_improvement_suggestions"]:
        st.header("Resume Improvements")
        st.write(result["resume_improvement_suggestions"])

    if result["learning_roadmap"]:
        st.header("Learning Roadmap")
        st.write(result["learning_roadmap"])

    st.header("Final Recommendation")
    st.write(result["final_recommendation"])