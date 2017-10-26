import sys
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.run_test_button = QtWidgets.QPushButton(testAreaBox)
        self.run_test_button.setObjectName("run_test_button")
        self.stop_test_button = QtWidgets.QPushButton(testAreaBox)
        self.stop_test_button.setObjectName("stop_test_button")
        self.fileName_lineEdit = QtWidgets.QLineEdit(testAreaBox)
        self.fileName_lineEdit.setReadOnly(True)
        self.fileName_lineEdit.setObjectName("fileName_lineEdit")
        # listView
        self.list = KakaQTextBrowser(testAreaBox)
        
        self.gridLayout.addWidget(self.lcdnumber, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.fileName_lineEdit, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.run_test_button, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.stop_test_button, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.list, 3, 0, 1, 2)
        
        self.run_test_button.clicked.connect(testAreaBox.on_run_test_button_clicked)
        self.stop_test_button.clicked.connect(testAreaBox.on_stop_test_button_clicked)


        self.retranslateUi(testAreaBox)

    def retranslateUi(self, testAreaBox):
        _translate = QtCore.QCoreApplication.translate
        testAreaBox.setTitle(_translate("TestAreaBox", "Test Area"))
        self.run_test_button.setText(_translate("PlotBox", "Run Test"))
        self.stop_test_button.setText(_translate("PlotBox", "Stop Test"))