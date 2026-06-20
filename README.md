# 📄 Resume Job Match AI

An AI-powered ATS (Applicant Tracking System) Resume Analyzer that compares a candidate’s resume with a job description and calculates job compatibility using skill matching and semantic analysis.

---

## 🚀 Live Demo

(Add your Streamlit deployed link here)

---

## 📌 Problem Statement

Recruiters often receive hundreds of resumes for a single job posting. Manually screening each resume is time-consuming and inefficient.

This project automates the process by:

* Extracting text from resumes
* Identifying technical skills
* Comparing resume skills with job requirements
* Calculating ATS compatibility score
* Suggesting missing skills for improvement

---

## ✨ Features

✅ Resume PDF Parsing
✅ Skill Extraction from Resume
✅ Job Description Analysis
✅ Keyword-Based Matching
✅ Semantic Matching
✅ ATS Score Calculation
✅ Missing Skill Detection
✅ AI Recommendations
✅ Downloadable PDF Report

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Matplotlib**
* **PDFPlumber**
* **FPDF**
* **NLP (Skill Matching)**

---

## 🧠 How It Works

1. Upload resume PDF
2. Paste job description
3. Extract resume text
4. Detect skills from both inputs
5. Calculate:

   * Keyword Match Score
   * Semantic Similarity Score
   * Final ATS Score
6. Generate AI suggestions
7. Download ATS report

---

## 📊 Scoring Logic

Final ATS Score is calculated using:

* 40% Keyword Matching
* 60% Semantic Similarity

Formula:

Final Score = (Keyword Score × 0.4) + (AI Score × 0.6)

---

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Analysis Dashboard

![Analysis Dashboard](screenshots/analysis.png)

### ATS Report Download

![Report Download](screenshots/report.png)

---

## 📁 Project Structure

```bash
resume-job-match-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── skills.csv
│
├── utils/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   ├── simple_ai_matcher.py
│   └── report_generator.py
│
└── screenshots/
```

---

## ⚙ Installation

```bash
git clone <your-repository-url>
cd resume-job-match-ai
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔮 Future Improvements

* OCR support for scanned resumes
* LLM-based semantic matching
* Support for DOCX resumes
* Resume improvement recommendations
* Cloud deployment with analytics

---

## 💼 Resume Impact

Built an AI-powered ATS Resume Analyzer using Python, NLP, and Streamlit to automate resume screening, skill-gap analysis, and candidate-job compatibility scoring.

---

## 👩‍💻 Author

**Akanksha Kumari Sinha**

* GitHub: https://github.com/akank275
* LinkedIn: Add your LinkedIn profile here
