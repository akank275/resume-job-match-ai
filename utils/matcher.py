def calculate_match(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return 0, set(), []

    matched = set(resume_skills).intersection(set(jd_skills))
    score = (len(matched) / len(jd_skills)) * 100
    missing_skills = list(set(jd_skills) - matched)

    return round(score, 2), matched, missing_skills