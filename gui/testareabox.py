from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTime, QTimer
from gui.ui_testareabox import Ui_TestAreaBox
import pytest
import subprocess
from subprocess import Popen, PIPE

class WorkThread(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)

        # Connect signal to the desired function
        
    def run(self):
        for i in range(300000000):
            continue
        self.sig.emit()

class TestAreaBox(QtWidgets.QGroupBox):

    trigger = pyqtSignal(['QString'])

    def __init__(self, parent=None):
        super(TestAreaBox, self).__init__(parent)

        self.trigger.connect(self.show_data)
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.show_time)
        self.__timer.start(1000)
        self.work_thread = WorkThread()
        self.work_thread.sig.connect(self.show_info)


        self.ui = Ui_TestAreaBox()
        self.ui.setupUi(self)
        self._setup_ui()

        self.ui.run_test1_button.clicked.connect(self.start)

    def _setup_ui(self):
        """ """
    
    def show_time(self):
        time = QTime.currentTime().toString("hh:mm:ss")
        self.ui.lcdnumber.display(time)
    
    def start(self):
        self.work_thread.start()

    def show_info(self):
        self.ui.fileName_lineEdit.setText('計算完畢')
        
    
    def on_run_test_button_clicked(self):
        self.ui.list.clear()
        p = subprocess.Popen(['pytest', '-p', 'no:terminal'], stdout=PIPE, stderr=PIPE)
        #pytest.main(['-p', 'no:terminal'])
        
        i = 0
        while True:
            i += 1
            line = p.stdout.readline().decode('UTF8')
            
            if line == '' and p.poll() != None:
                break
            elif line != '':
                self.trigger.emit(line)
            else:
                break
                      
        p.kill()
    
    @pyqtSlot(str)
    def show_data(self, line):
        self.ui.list.insertPlainText(line)
        self.ui.list.show()
