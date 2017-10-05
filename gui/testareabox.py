from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from gui.ui_testareabox import Ui_TestAreaBox
import pytest
import subprocess
from subprocess import Popen, PIPE

class TestAreaBox(QtWidgets.QGroupBox):

    trigger = pyqtSignal(['QString'])

    def __init__(self, parent=None):
        super(TestAreaBox, self).__init__(parent)

        self.trigger.connect(self.show_data)

        self.ui = Ui_TestAreaBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
    
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
