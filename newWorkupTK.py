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
        super().__init__(master)
        self.master = master

        # variable definitions
        self.dataDir    = tk.StringVar(self, value="/Users/yanxlin/github/workupsoftware/test/in")
        self.odnpFile   = tk.StringVar(self, value="/Users/yanxlin/github/workupsoftware/test/in/180329_HttQ25_30R1_22C_ODNP_3")
        self.t1File     = tk.StringVar(self)
        self.eprFile    = tk.StringVar(self)
        self.eprCalFile = tk.StringVar(self)

        # create widgets
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Load Data Directory", command=self.DataDirOpened).pack()
        tk.Entry(self, textvariable=self.dataDir).pack()
        tk.Button(self, text="Load ODNP Folder", command=self.ODNPOpened).pack()
        tk.Entry(self, textvariable=self.odnpFile).pack()
        tk.Button(self, text="Load T1 File", command=self.T1Opened).pack()
        tk.Entry(self, textvariable=self.t1File).pack()
        tk.Button(self, text="Load EPR File", command=self.EPROpened).pack()
        tk.Entry(self, textvariable=self.eprFile).pack()
        tk.Button(self, text="Load EPR Calibration File", command=self.EPRCalOpened).pack()
        tk.Entry(self, textvariable=self.eprCalFile).pack()
        tk.Button(self, text="run", command=self.runProgram).pack()
        tk.Button(self, text="save data", command=self.saveDataDir).pack()
        tk.Button(self, text="save calibration", command=self.saveCalFile).pack()
        tk.Button(self, text="exit", command=self.exitProgram).pack()

    def DataDirOpened(self):
        """ Handling to open the file browser to choose the data directory """
        self.dataDir.set(tkfd.askdirectory())
        self.DataDir = self.dataDir.get()

    def dbComboChanged(self):
        """ Handling for the database combo box """
        raise PendingDeprecationWarning

    def ODNPOpened(self):
        """ Handling for the ODNP file browser button """
        self.odnpFile.set(tkfd.askdirectory(
            initialdir=self.dataDir.get() if self.dataDir.get() else os.getcwd()))
        self.ODNPFile = self.odnpFile.get()

    def T1Opened(self):
        """ Handling for the T1 file browser button """
        self.t1File.set(tkfd.askopenfilename(
            initialdir=self.dataDir.get() if self.dataDir.get() else os.getcwd()))

    def EPROpened(self):
        """ Handling for the EPR file browser button """
        self.eprFile.set(tkfd.askopenfilename(
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
        # Initialize the workup script
        self.retInt = returnIntegralsDev.workupODNP()

        # variable definitions from last version  # TODO: // remove this chunk
        self.DataDir    = self.dataDir.get()
        self.ODNPFile   = self.odnpFile.get()
        self.T1File     = self.t1File.get()
        self.EPRFile    = self.eprFile.get()
        self.EPRCalFile = self.eprCalFile.get()
        self.retInt.DataDir    = self.DataDir
        self.retInt.ODNPFile   = self.ODNPFile
        self.retInt.T1File     = self.T1File
        self.retInt.EPRFile    = self.EPRFile
        self.retInt.EPRCalFile = self.EPRCalFile

        self.dataBase = False  # TODO: // remove this chunk
        self.dataDirFile = 'datadir.txt'
        self.calSaveFile = 'calFile.txt'
        self.dataBaseList = ['Select Value','Yes','No']#}}}

        self.runExperiment()
        self.refreshDisplay()

    def runExperiment(self):
        """ Make the calls to run the odnp experimental workup from 
        returnIntegralsDev """
        self.retInt.determine_exp_type()
        # self.retInt.editDatabase()
        if self.retInt.isNMRExp: self.retInt.set_exp_numbers()
        self.retInt.returnExpParamsDict()
        ### # if self.retInt.nmrExp: self.retInt.determineExperiment() # Should no longer be needed, hang on to incase you need something.
        ### # else: print "EPR Experiment"
        ### # self.retInt.determineDatabase()
        ### On windows you cannot run from the command line any interaction with raw_input is rejected
        if self.retInt.isNMRExp: self.retInt.readSpecType()
        if self.retInt.isNMRExp: self.retInt.editExpDict()
        if self.retInt.isEPRExp: self.retInt.editExpDictEPR()
        # if self.retInt.writeToDB: self.retInt.editDatabaseDict()
        returnIntegralsDev.makeTitle("  Running Workup  ")
        if self.retInt.isEPRExp: self.retInt.returnEPRData()
        if self.retInt.isDNPExp: self.retInt.dnpPowers()
        if self.retInt.isDNPExp: self.retInt.enhancementIntegration()
        if self.retInt.isNMRExp: self.retInt.T1Integration()
        if self.retInt.isDNPExp: self.retInt.makeT1PowerSeries()
        if self.retInt.isDNPExp: self.retInt.compKsigma()
        if self.dataBase: self.retInt.writeToDatabase()
        self.retInt.dumpAllToCSV()
        self.retInt.writeExpParams()
        returnIntegralsDev.compilePDF(self.retInt.expName, self.retInt.odnpName,
                                      self.retInt.fl)

root = tk.Tk()
app = initialWindow(master=root)
app.mainloop()
