import os
import wx
import pdfplumber
import csv

wildcard = "Portable Document Format(*.pdf)|*.pdf|" \
            "All files (*.*)|*.*"

wildcards = "Comma Separated Values source (*.csv)|*.csv|" \
            "All files (*.*)|*.*"

########################################################################
class MyForm(wx.Frame):

#----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "AO DATA Conversion")
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        openFileDlgBtn = wx.Button(panel, label="OPEN PDF FILE PATH")
        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)

        saveFileDlgBtn = wx.Button(panel, label="SAVE DATA FILE PATH")
        saveFileDlgBtn.Bind(wx.EVT_BUTTON, self.onSaveFile)

        ExecuteFileDlgBtn = wx.Button(panel, label="EXECUTE DATA EXTRACTION")
        ExecuteFileDlgBtn.Bind(wx.EVT_BUTTON, self.onExecuteFile)

        # put the buttons in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(openFileDlgBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(saveFileDlgBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(ExecuteFileDlgBtn, 0, wx.ALL|wx.CENTER, 8)
        panel.SetSizer(sizer)
#----------------------------------------------------------------------
    def onOpenFile(self, event):
        """
        Create and show the OPEN FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Open file as ...", 
            defaultDir=self.currentDirectory, 
            defaultFile="", wildcard=wildcard, style=wx.FD_OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print ("You chose the following filename: %s" % path)
            
        #dlg.Destroy()

#----------------------------------------------------------------------
#----------------------------------------------------------------------
    def onSaveFile(self, event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Save file as ...", 
            defaultDir=self.currentDirectory, 
            defaultFile="", wildcard=wildcards, style=wx.FD_SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path1 = dlg.GetPath()
            print ("You chose the following filename: %s" % path1)
            
        #dlg.Destroy()

#----------------------------------------------------------------------
#----------------------------------------------------------------------
    def onExecuteFile(self, event):
        """
        Create and show the Execute FileDialog
        """

        outfile = open(path1, 'w')
        outcsv = csv.writer(outfile)

        with pdfplumber.open(path) as pdf:
            first_page = pdf.pages[0]
            table = first_page.extract_table()
            for row in table[0:]:
                outcsv.writerow(row)
                outfile.close 

#----------------------------------------------------------------------            
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
