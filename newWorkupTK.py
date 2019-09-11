"""
This script rewrites "newWorkup.py" by using tkinter instead of PyQt4
"""
import returnIntegralsDev
# import test
import sys, os
import tkinter as tk
import tkinter.filedialog as tkfd

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
        # Initialize the workup script
        self.retInt = returnIntegralsDev.workupODNP(self)

        # variable definitions
        self.dataDir    = tk.StringVar()
        self.odnpFile   = tk.StringVar()
        self.t1File     = tk.StringVar()
        self.eprFile    = tk.StringVar()
        self.eprCalFile = tk.StringVar()

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="load data dir", command=self.DataDirOpened).pack()
        tk.Entry(self, textvariable=self.dataDir).pack()
        tk.Button(self, text="load ODNP file", command=self.ODNPOpened).pack()
        tk.Entry(self, textvariable=self.odnpFile).pack()
        tk.Button(self, text="load T1 file", command=self.T1Opened).pack()
        tk.Entry(self, textvariable=self.t1File).pack()
        tk.Button(self, text="load EPR file", command=self.EPROpened).pack()
        tk.Entry(self, textvariable=self.eprFile).pack()
        tk.Button(self, text="load EPR Calibration file", command=self.EPRCalOpened).pack()
        tk.Entry(self, textvariable=self.eprCalFile).pack()
        tk.Button(self, text="run", command=self.runProgram).pack()
        tk.Button(self, text="save data", command=self.saveDataDir).pack()
        tk.Button(self, text="save calibration", command=self.saveCalFile).pack()
        tk.Button(self, text="exit", command=self.exitProgram).pack()

    def DataDirOpened(self):
        """ Handling to open the file browser to choose the data directory """
        self.dataDir.set(tkfd.askdirectory())

    def dbComboChanged(self):
        """ Handling for the database combo box """
        raise PendingDeprecationWarning

    def ODNPOpened(self):
        """ Handling for the ODNP file browser button """
        self.odnpFile.set(tkfd.askdirectory(
            initialdir=self.dataDir.get() if self.dataDir.get() else os.getcwd()))

    def T1Opened(self):
        """ Handling for the T1 file browser button """
        self.t1File.set(tkfd.askdirectory(
            initialdir=self.dataDir.get() if self.dataDir.get() else os.getcwd()))

    def EPROpened(self):
        """ Handling for the EPR file browser button """
        self.eprFile.set(tkfd.askdirectory(
            initialdir=self.dataDir.get() if self.dataDir.get() else os.getcwd()))

    def EPRCalOpened(self):  # {{{
        """ Handling for the EPR Calibration file browser button """
        self.eprCalFile.set(tkfd.askdirectory(
            initialdir=self.dataDir.get() if self.dataDir.get() else os.getcwd()))

    def saveDataDir(self):
        """ Handling for the save data directory button """
        raise PendingDeprecationWarning

    def saveCalFile(self):  # {{{
        """ Handling for the save calibration data button """
        raise PendingDeprecationWarning

    def refreshDisplay(self):#{{{
        """ Reset all display stuff for another go """
        # TODO:// Implement this
        pass

    def exitProgram(self):#{{{
        """ Handling for to exit the program """
        self.master.destroy()

    def runProgram(self):  # {{{  TODO:// merge with runExperiment
        """ Handling for the run program button to launch the return integrals 
        workup program """
        self.runExperiment()
        self.refreshDisplay()

    def runExperiment(self):
        """ Make the calls to run the odnp experimental workup from 
        returnIntegralsDev """
        self.retInt.determineExpType()
        self.retInt.editDatabase()
        if self.retInt.nmrExp: self.retInt.returnExpNumbers()
        self.retInt.returnExpParamsDict()
        ### # if self.retInt.nmrExp: self.retInt.determineExperiment() # Should no longer be needed, hang on to incase you need something.
        ### # else: print "EPR Experiment"
        ### # self.retInt.determineDatabase()
        ### On windows you cannot run from the command line any interaction with raw_input is rejected
        if self.retInt.nmrExp: self.retInt.readSpecType()
        if self.retInt.nmrExp: self.retInt.editExpDict()
        if self.retInt.eprExp: self.retInt.editExpDictEPR()
        # if self.retInt.writeToDB: self.retInt.editDatabaseDict()
        returnIntegralsDev.makeTitle("  Running Workup  ")
        if self.retInt.eprExp: self.retInt.returnEPRData()
        if self.retInt.dnpexp: self.retInt.dnpPowers()
        if self.retInt.dnpexp: self.retInt.enhancementIntegration()
        if self.retInt.nmrExp: self.retInt.T1Integration()
        if self.retInt.dnpexp: self.retInt.makeT1PowerSeries()
        if self.retInt.dnpexp: self.retInt.compKsigma()
        if self.dataBase: self.retInt.writeToDatabase()
        self.retInt.dumpAllToCSV()
        self.retInt.writeExpParams()
        returnIntegralsDev.compilePDF(self.retInt.name, self.retInt.odnpName,
                                      self.retInt.fl)

root = tk.Tk()
app = initialWindow(master=root)
app.mainloop()
