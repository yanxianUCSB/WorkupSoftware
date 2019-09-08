"""
This script rewrites "newWorkup.py" by using tkinter instead of PyQt4
"""
import sys, os
import tkinter as tk

#{ class for calling and running the GUI dialog
class initialWindow(tk.Frame):  # TODO: rename as "ODNP_Analyzer"
    """
    This opens a window which has access to file dialogs for choosing the 
    dataDirectory, the ODNP experiment directory, the T1 experiment directory, 
    and the EPR experiment file location.

    This passes all of the parent class variables and definitions on to the 
    child class workupODNP located in returnIntegralsDev.py
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="load data dir", command=self.DataDirOpened).pack()
        tk.Entry(self, textvariable="dataDir").pack()
        tk.Button(self, text="load ODNP file", command=self.ODNPOpened).pack()
        tk.Entry(self, textvariable="ODNPfile").pack()
        tk.Button(self, text="load T1 file", command=self.T1Opened).pack()
        tk.Entry(self, textvariable="T1file").pack()
        tk.Button(self, text="load EPR file", command=self.EPROpened).pack()
        tk.Entry(self, textvariable="eprFile").pack()
        tk.Button(self, text="load EPR Calibration file", command=self.EPRCalOpened).pack()
        tk.Entry(self, textvariable="eprCalFile").pack()
        tk.Button(self, text="run", command=self.runProgram).pack()
        tk.Button(self, text="save data", command=self.saveDataDir).pack()
        tk.Button(self, text="save calibration", command=self.saveCalFile).pack()
        tk.Button(self, text="exit", command=self.exitProgram).pack()
        pass

    def DataDirOpened(self):
        """ Handling to open the file browser to choose the data directory """
        pass

    def dbComboChanged(self):
        """ Handling for the database combo box """
        print("This does nothing anymore.")

    def ODNPOpened(self):
        """ Handling for the ODNP file browser button """
        pass

    def T1Opened(self):
        """ Handling for the T1 file browser button """
        pass

    def EPROpened(self):
        """ Handling for the EPR file browser button """
        pass

    def EPRCalOpened(self):  # {{{
        """ Handling for the EPR Calibration file browser button """
        pass

    def saveDataDir(self):
        """ Handling for the save data directory button """
        pass

    def saveCalFile(self):  # {{{
        """ Handling for the save calibration data button """
        pass

    def refreshDisplay(self):#{{{
        """ Reset all display stuff for another go """
        pass

    def exitProgram(self):#{{{
        """ Handling for to exit the program """
        pass

    def runProgram(self):  # {{{
        """ Handling for the run program button to launch the return integrals 
        workup program """
        pass

    def runExperiment(self):  # {{{
        """ Make the calls to run the odnp experimental workup from 
        returnIntegralsDev """
        pass

root = tk.Tk()
app = initialWindow(master=root)
app.mainloop()