from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def bert_match(resume_text, jd_text):

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    jd_embedding = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        resume_embedding,
        jd_embedding
    )

    score = similarity.item() * 100

    return round(score, 2)