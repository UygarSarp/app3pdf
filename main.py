from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics1.csv")
pdf = FPDF(orientation="P", unit="mm", format="a4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=32)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")
