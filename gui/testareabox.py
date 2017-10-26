import sys
import time
import pytest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QTime, QTimer
from gui.ui_testareabox import Ui_TestAreaBox

class Worker(QObject):
    """ Pytest Thread """

    #sig = pyqtSignal(['QString'])
    sig = pyqtSignal(int)
    sig_done = pyqtSignal()

    def __init__(self, path=None):
        super().__init__()

        self.path = path

    @pyqtSlot()
    def work(self):
        pytest.main(['-p', 'no:terminal'])

        """
        for i in range(100):
            time.sleep(0.1)
            self.sig.emit(i)
        """

        self.sig_done.emit()
    
            
class TestAreaBox(QtWidgets.QGroupBox): 
    def __init__(self, parent=None):
        super(TestAreaBox, self).__init__(parent)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.show_time)
        self.__timer.start(1000)

        self.__threads = None

        self.ui = Ui_TestAreaBox()
        self.ui.setupUi(self)
        self._setup_ui()

    def _setup_ui(self):
        """ """
    
    def show_time(self):
        time = QTime.currentTime().toString("hh:mm:ss")
        self.ui.lcdnumber.display(time)
    
    def on_run_test_button_clicked(self):
        """ Pytest Thread Start """

        self.__threads = []
        worker = Worker()
        thread = QThread(self)
        self.__threads.append((thread, worker))  # need to store worker too otherwise will be gc'd
        worker.moveToThread(thread)

        worker.sig.connect(self.show_info)
        worker.sig_done.connect(self.on_worker_done)

        # control worker:
        #self.sig_abort_workers.connect(worker.abort)

        thread.started.connect(worker.work)
        thread.start()
    
    def on_stop_test_button_clicked(self):
        '''
        self.sig_abort_workers.emit()

        for thread, worker in self.__threads:
            thread.quit()
            thread.wait()
        
        print('Stop!!!')
        '''

    def on_worker_done(self):
        for thread, Worker in self.__threads:
            thread.quit()
            thread.wait()
        
    
    def show_info(self, i):
        self.ui.list.insertPlainText(str(i))
        self.ui.list.insertPlainText('\n')
        self.ui.list.show()
    

