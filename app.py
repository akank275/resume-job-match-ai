import streamlit as st
import matplotlib.pyplot as plt

from utils.resume_parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_match
from utils.simple_ai_matcher import semantic_match
from utils.report_generator import generate_report

st.set_page_config(page_title="Resume Job Match AI")

st.title("📄 Resume Job Match AI")

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if resume_file and job_description:

        # Extract resume text
        resume_text = extract_resume_text(resume_file)

        # AI score
        ai_score = semantic_match(
            resume_text,
            job_description
        )

        # Extract skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        st.write("Resume Text Preview:", resume_text[:500])
        st.write("Resume Skills:", resume_skills)
        st.write("JD Skills:", jd_skills)

        # Calculate scores
        score, matched, missing = calculate_match(
            resume_skills,
            jd_skills
        )

        final_score = (score * 0.4) + (ai_score * 0.6)

        # Match quality
        if final_score >= 80:
            st.success("Strong Match")
        elif final_score >= 60:
            st.warning("Moderate Match")
        else:
            st.error("Low Match")

        # Generate report
        report_file = generate_report(
            round(final_score, 2),
            score,
            ai_score,
            matched,
            missing
        )

        # Score display
        st.subheader("Keyword Match Score")
        st.metric("Keyword Score", f"{score}%")

        st.subheader("AI Semantic Score")
        st.metric("Semantic Similarity", f"{ai_score}%")

        st.subheader("Final ATS Score")
        st.metric("Final Score", f"{round(final_score, 2)}%")

        st.progress(int(final_score))

        # Matched skills
        st.subheader("Matched Skills")
        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.info("No matched skills found.")

        # Missing skills
        st.subheader("Missing Skills")
        if missing:
            for skill in missing:
                st.error(skill)
        else:
            st.success("No missing skills.")

        # Pie chart
        labels = ["Matched", "Missing"]
        sizes = [len(matched), len(missing)]

        if sum(sizes) > 0:
            fig, ax = plt.subplots()
            ax.pie(
                sizes,
                labels=labels,
                autopct="%1.1f%%"
            )
            st.pyplot(fig)
        else:
            st.info("No skill data available for chart.")

        # Suggestions
        st.subheader("AI Suggestions")
        if missing:
            for skill in missing:
                st.warning(
                    f"Consider adding projects or certifications related to {skill}"
                )
        else:
            st.success("Excellent profile for this role.")

        # Resume skills
        st.subheader("Resume Skills")
        st.write(resume_skills)

        # Download report
        with open(report_file, "rb") as file:
            st.download_button(
                label="Download ATS Report",
                data=file,
                file_name="ats_report.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("Upload resume and paste job description.")