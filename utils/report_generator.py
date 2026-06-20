from fpdf import FPDF


def generate_report(
    final_score,
    keyword_score,
    ai_score,
    matched,
    missing
):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Resume ATS Report", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(
        200,
        10,
        f"Final ATS Score: {final_score}%",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Keyword Score: {keyword_score}%",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"AI Score: {ai_score}%",
        ln=True
    )

    pdf.cell(200, 10, "Matched Skills:", ln=True)

    for skill in matched:
        pdf.cell(200, 10, f"- {skill}", ln=True)

    pdf.cell(200, 10, "Missing Skills:", ln=True)

    for skill in missing:
        pdf.cell(200, 10, f"- {skill}", ln=True)

    file_name = "ats_report.pdf"
    pdf.output(file_name)

    return file_name