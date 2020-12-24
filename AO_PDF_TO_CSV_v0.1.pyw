import PySimpleGUI as sg
import pdfplumber
import csv

loop = True

while (loop):

    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [  [sg.Text('Select a PDF FILE')],
                [sg.Input(), sg.FileBrowse(file_types=(("pdf file", "*.pdf"),))],
                [sg.Text('Save a CSV filename')],
                [sg.Input(), sg.FileSaveAs(file_types=(("csv file", "*.csv"),))], 
                [sg.OK(), sg.Cancel()]] 

    window = sg.Window('PDF TO CSV FILE EXTRACTION', layout)

    event, values = window.read()

    if event == "OK" and len(values[0])!= 0 and len(values[1]) != 0:
        outfile = open(values[1], 'w')
        outcsv = csv.writer(outfile)

        with pdfplumber.open(values[0]) as pdf:
            first_page = pdf.pages[0]
            table = first_page.extract_table()
            for row in table[0:]:
                outcsv.writerow(row)
            outfile.close
        
        sg.popup('CONVERSION COMPLETED, Exit program')
        loop = True
        

    elif event == "Cancel":

        sg.popup('OPERATION TERMINATED')
        break

    elif len(values[0])== 0 or len(values[1]) == 0:

        sg.popup_error('INPUT IS MISSING, TERMINATING PROGRAM. CONTACT YOUR SYSTEM ADMINISTRATOR.')
        loop = True    

    else: 
        sg.popup_error('UNKNOWN INPUT, TERMINATING PROGRAM. CONTACT YOUR SYSTEM ADMINISTRATOR.')
        break



    window.close()