import pandas as pd

skills_db = pd.read_csv("data/skills.csv")

skill_list = skills_db["skill"].tolist()


def extract_skills(text):

    found_skills = []

    for skill in skill_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))