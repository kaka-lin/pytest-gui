from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys

class KakaQTextBrowser(QtWidgets.QTextBrowser):
    def __init__(self, parent=None):
        super(KakaQTextBrowser, self).__init__(parent)
    
    def write(self, text):
        self.insertPlainText(text)

    def flush(self):
        sys.stdout.flush
    
    def buffer(self):
        sys.stdout.buffer
    
    def isatty(self):
        sys.stdout.isatty


class Ui_TestAreaBox(object):
    def setupUi(self, testAreaBox):
        testAreaBox.setObjectName("testAreaBox")

        self.gridLayout = QtWidgets.QGridLayout(testAreaBox)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(12)

        self.lcdnumber = QtWidgets.QLCDNumber(testAreaBox)
        self.lcdnumber.setObjectName("lcdnumber")
        self.lcdnumber.setDigitCount(8)
        self.lcdnumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.run_test1_button = QtWidgets.QPushButton(testAreaBox)
        self.run_test1_button.setObjectName("run_test1_button")
        self.fileName_lineEdit = QtWidgets.QLineEdit(testAreaBox)
        self.fileName_lineEdit.setReadOnly(True)
        self.fileName_lineEdit.setObjectName("fileName_lineEdit")
        # listView
        self.list = KakaQTextBrowser(testAreaBox)
        
        self.gridLayout.addWidget(self.lcdnumber, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.fileName_lineEdit, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.run_test1_button, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.list, 2, 0, 1, 2)
        
        self.retranslateUi(testAreaBox)

    def retranslateUi(self, testAreaBox):
        _translate = QtCore.QCoreApplication.translate
        testAreaBox.setTitle(_translate("TestAreaBox", "Test Area"))
        self.run_test1_button.setText(_translate("PlotBox", "Run Test"))