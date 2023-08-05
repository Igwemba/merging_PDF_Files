from PyPDF2 import PdfMerger

pdfs = ['BANK LETTER.pdf', 'Board Resoltuin.pdf', 'TCC 2021.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write('merged_igwemba.pdf')
merger.close()
