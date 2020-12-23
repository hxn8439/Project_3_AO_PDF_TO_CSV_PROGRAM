import pdfplumber
import csv

outfile = open('test1.csv', 'w')
outcsv = csv.writer(outfile)

with pdfplumber.open("C:/Users/dienadel/Desktop/perfecttable.pdf") as pdf:
    first_page = pdf.pages[0]
    table = first_page.extract_table()
    for row in table[0:]:
        outcsv.writerow(row)
    outfile.close    