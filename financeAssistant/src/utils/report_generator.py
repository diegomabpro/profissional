from fpdf import FPDF
from datetime import datetime

def generate_report(data, filename="report.pdf"):
    """
    Gera um relatório em PDF com os resultados das análises.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título
    pdf.cell(200, 10, txt="Relatório de Análise Financeira", ln=True, align="C")
    pdf.ln(10)

    # Data e Hora
    pdf.cell(200, 10, txt=f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)

    # Resultados das Análises
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    # Salva o PDF
    pdf.output(filename)