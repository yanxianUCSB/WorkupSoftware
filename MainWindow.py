# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Jun 19 13:33:52 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(747, 608)
        mainWindow.setAutoFillBackground(True)
        self.frame = QtGui.QFrame(mainWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 721, 581))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 510, 641, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.saveDirButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.saveDirButton.setObjectName(_fromUtf8("saveDirButton"))
        self.gridLayout.addWidget(self.saveDirButton, 0, 0, 1, 1)
        self.runButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.gridLayout.addWidget(self.runButton, 0, 3, 1, 1)
        self.exitButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.gridLayout.addWidget(self.exitButton, 0, 2, 1, 1)
        self.saveCalButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.saveCalButton.setObjectName(_fromUtf8("saveCalButton"))
        self.gridLayout.addWidget(self.saveCalButton, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 441, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.directoryTitle = QtGui.QLabel(self.verticalLayoutWidget)
        self.directoryTitle.setObjectName(_fromUtf8("directoryTitle"))
        self.verticalLayout_2.addWidget(self.directoryTitle, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.DataDirDisplay = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.DataDirDisplay.setObjectName(_fromUtf8("DataDirDisplay"))
        self.horizontalLayout.addWidget(self.DataDirDisplay)
        self.DataDirOpenBrowser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.DataDirOpenBrowser.setObjectName(_fromUtf8("DataDirOpenBrowser"))
        self.horizontalLayout.addWidget(self.DataDirOpenBrowser)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.ODNPTitle = QtGui.QLabel(self.verticalLayoutWidget)
        self.ODNPTitle.setObjectName(_fromUtf8("ODNPTitle"))
        self.verticalLayout_2.addWidget(self.ODNPTitle, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ODNPDisplay = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.ODNPDisplay.setObjectName(_fromUtf8("ODNPDisplay"))
        self.horizontalLayout_3.addWidget(self.ODNPDisplay)
        self.ODNPOpenBrowser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ODNPOpenBrowser.setObjectName(_fromUtf8("ODNPOpenBrowser"))
        self.horizontalLayout_3.addWidget(self.ODNPOpenBrowser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.T1Title = QtGui.QLabel(self.verticalLayoutWidget)
        self.T1Title.setObjectName(_fromUtf8("T1Title"))
        self.verticalLayout_2.addWidget(self.T1Title, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.T1Display = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.T1Display.setObjectName(_fromUtf8("T1Display"))
        self.horizontalLayout_6.addWidget(self.T1Display)
        self.T1OpenBrowser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.T1OpenBrowser.setObjectName(_fromUtf8("T1OpenBrowser"))
        self.horizontalLayout_6.addWidget(self.T1OpenBrowser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.EPRTitle = QtGui.QLabel(self.verticalLayoutWidget)
        self.EPRTitle.setObjectName(_fromUtf8("EPRTitle"))
        self.verticalLayout_2.addWidget(self.EPRTitle, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.EPRFileDisplay = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.EPRFileDisplay.setObjectName(_fromUtf8("EPRFileDisplay"))
        self.horizontalLayout_4.addWidget(self.EPRFileDisplay)
        self.EPROpenBrowser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.EPROpenBrowser.setObjectName(_fromUtf8("EPROpenBrowser"))
        self.horizontalLayout_4.addWidget(self.EPROpenBrowser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.EPRCalTitle = QtGui.QLabel(self.verticalLayoutWidget)
        self.EPRCalTitle.setObjectName(_fromUtf8("EPRCalTitle"))
        self.verticalLayout_2.addWidget(self.EPRCalTitle, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.EPRCalFileDisplay = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.EPRCalFileDisplay.setObjectName(_fromUtf8("EPRCalFileDisplay"))
        self.horizontalLayout_5.addWidget(self.EPRCalFileDisplay)
        self.EPRCalOpenBrowser = QtGui.QPushButton(self.verticalLayoutWidget)
        self.EPRCalOpenBrowser.setObjectName(_fromUtf8("EPRCalOpenBrowser"))
        self.horizontalLayout_5.addWidget(self.EPRCalOpenBrowser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(490, 130, 181, 61))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.databaseComboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.databaseComboBox.setObjectName(_fromUtf8("databaseComboBox"))
        self.gridLayout_2.addWidget(self.databaseComboBox, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.title = QtGui.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(0, 40, 721, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans Typewriter"))
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setObjectName(_fromUtf8("title"))
        self.textBrowser = QtGui.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(470, 200, 231, 291))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "mainWindow", None))
        self.saveDirButton.setText(_translate("mainWindow", "Save Data Directory", None))
        self.runButton.setText(_translate("mainWindow", "Run Workup", None))
        self.exitButton.setText(_translate("mainWindow", "Exit", None))
        self.saveCalButton.setText(_translate("mainWindow", "Save Calibration File", None))
        self.directoryTitle.setText(_translate("mainWindow", "Data Directory", None))
        self.DataDirDisplay.setText(_translate("mainWindow", "Enter File Name", None))
        self.DataDirOpenBrowser.setText(_translate("mainWindow", "Browse", None))
        self.ODNPTitle.setText(_translate("mainWindow", "ODNP Folder Name", None))
        self.ODNPDisplay.setText(_translate("mainWindow", "Enter File Name", None))
        self.ODNPOpenBrowser.setText(_translate("mainWindow", "Browse", None))
        self.T1Title.setText(_translate("mainWindow", "T1 Folder Name", None))
        self.T1Display.setText(_translate("mainWindow", "Enter File Name", None))
        self.T1OpenBrowser.setText(_translate("mainWindow", "Browse", None))
        self.EPRTitle.setText(_translate("mainWindow", "EPR File Name", None))
        self.EPRFileDisplay.setText(_translate("mainWindow", "Enter File Name", None))
        self.EPROpenBrowser.setText(_translate("mainWindow", "Browse", None))
        self.EPRCalTitle.setText(_translate("mainWindow", "EPR Calibration File Name", None))
        self.EPRCalFileDisplay.setText(_translate("mainWindow", "Enter File Name", None))
        self.EPRCalOpenBrowser.setText(_translate("mainWindow", "Browse", None))
        self.label.setText(_translate("mainWindow", "Write Data To Database?", None))
        self.title.setText(_translate("mainWindow", "ODNP T1 and EPR Experiment Workup", None))
