import pdfplumber
import csv

outfile = open('/Users/dienadel/Desktop/test2.csv', 'w')
outcsv = csv.writer(outfile)

with pdfplumber.open("C:/Users/dienadel/Desktop/AOProgram/PDFtoCSV/perfecttable.pdf") as pdf:
    first_page = pdf.pages[0]
    table = first_page.extract_table()
    for row in table[0:]:
        outcsv.writerow(row)
    outfile.close    