from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=24)
pdf.cell(0, 10, "CS50 Shirtificate", align="C", ln=1)
pdf.ln(10)
pdf.image(
    "shirtificate.png",
    x=10,
    y=50,
    w=pdf.w - 20,
)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 145)
pdf.cell(0, 10, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
