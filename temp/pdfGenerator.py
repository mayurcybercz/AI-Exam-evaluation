# header_footer.py
 
from fpdf import FPDF
 
class CustomPDF(FPDF):
 
    def header(self):
        # Logo
        self.image('logo.png', 10, 8, 33)
		# Arial bold 15
        self.set_font('Arial', 'B', 15)
		# Move to the right
        self.cell(80)
		# Title
        self.cell(30, 10, 'Paper Title', 1, 0, 'C')
		# Line break
        self.ln(20)
 
    def footer(self):
        self.set_y(-10)
 
        self.set_font('Arial', 'I', 8)
 
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')
 
def create_pdf(pdf_path):
    pdf = CustomPDF()
    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1, 41):
        pdf.cell(0, 10, 'Printing question from csv file Q no'  + str(i),0,1)
        pdf.cell(0, 50, '',1,1)

    pdf.output('paper.pdf', 'F')
 
if __name__ == '__main__':
    create_pdf('header_footer.pdf')