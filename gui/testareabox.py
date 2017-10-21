import sys
import time
import pytest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTime, QTimer
from gui.ui_testareabox import Ui_TestAreaBox

class WorkThread(QtCore.QThread):
    # Create the signal
    sig = pyqtSignal(['QString'])

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        """ """

    def run(self):
        pytest.main(['-p', 'no:terminal'])
        

class TestAreaBox(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super(TestAreaBox, self).__init__(parent)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.show_time)
        self.__timer.start(1000)
        self.work_thread = WorkThread()

        self.ui = Ui_TestAreaBox()
        self.ui.setupUi(self)
        self._setup_ui()

        self.work_thread.sig.connect(self.show_info)
        self.ui.run_test1_button.clicked.connect(self.start)

    def _setup_ui(self):
        """ """
    
    def show_time(self):
        time = QTime.currentTime().toString("hh:mm:ss")
        self.ui.lcdnumber.display(time)
    
    def start(self):
        origin_stdout = sys.stdout
        sys.stdout = self.ui.list
        self.work_thread.start()
        #sys.stdout = origin_stdout
        #print('end')

    def show_info(self, line):
        self.ui.list.insertPlainText(line)
        self.ui.list.insertPlainText('\n')
        self.ui.list.show()
        