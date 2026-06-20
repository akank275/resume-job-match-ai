import re

def semantic_match(resume_text, jd_text):

    stop_words = {
        "need", "with", "and", "or", "the",
        "a", "an", "for", "to", "in"
    }

    resume_words = set(
        re.findall(r'\b\w+\b', resume_text.lower())
    ) - stop_words

    jd_words = set(
        re.findall(r'\b\w+\b', jd_text.lower())
    ) - stop_words

    if not jd_words:
        return 0

    common_words = resume_words.intersection(jd_words)

    score = (len(common_words) / len(jd_words)) * 100

    return round(score, 2)