from fpdf import FPDF

def main():
    
    pdfize(input("Name: "))

def pdfize(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", style="B", size=35)
    pdf.cell(0, 30, "CS50 Shirtificate", border=0, align="C")
    pdf.ln(100)

    pdf.image ("./shirtificate.png", 15, 50, 180)
    
    pdf.set_font("helvetica", style="B", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 20, f"{name} took CS50", border=0, align="C")
    
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()