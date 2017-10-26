import sys
import time
import queue
import pytest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QTime, QTimer
from PyQt5.QtWidgets import QApplication
from gui.ui_testareabox import Ui_TestAreaBox

origin_stdout = ''

class WriteStream(QObject):
    trigger = pyqtSignal()
    def __init__(self, queue, parent=None):
        super(WriteStream, self).__init__(parent)
        
        self.queue = queue

    def write(self, text):
        self.queue.put(text)
        self.trigger.emit()

    def flush(self):
        sys.stdout.flush
    
    def buffer(self):
        sys.stdout.buffer
    
    def isatty(self):
        sys.stdout.isatty
        

class Worker(QObject):
    """ Pytest Thread """

    sig_done = pyqtSignal()
    sig_msg = pyqtSignal(['QString'])

    def __init__(self, path=None, parent=None):
        super(Worker, self).__init__(parent)

        self.path = path

        self.queue = queue.Queue()
        self.writeStream = WriteStream(self.queue)

        self.__abort = False
        
        
    @pyqtSlot()
    def work(self):
        global origin_stdout
        origin_stdout = sys.stdout
        self.writeStream.trigger.connect(self.on_item_change)
        sys.stdout = self.writeStream
        pytest.main(['-p', 'no:terminal'])

        '''
        for step in range(100):
            time.sleep(0.1)
            print(step)
                
            QApplication.processEvents()
            if self.__abort:
                break
        '''
        
        self.sig_done.emit()
    
    def abort(self):
        self.__abort = True
    
    def on_item_change(self):
        while True:
            if self.queue.empty():
                break

            line = self.queue.get()
            
            if line == '\n':
                pass
            else:
                self.sig_msg.emit(line)
            
class TestAreaBox(QtWidgets.QGroupBox):

    sig_abort_workers = pyqtSignal()

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
        self.ui.list.clear()

        self.__threads = []
        worker = Worker()
        thread = QThread(self)
        self.__threads.append((thread, worker))  # need to store worker too otherwise will be gc'd
        worker.moveToThread(thread)

        worker.sig_done.connect(self.on_worker_done)
        worker.sig_msg.connect(self.show_info)

        # control worker:
        self.sig_abort_workers.connect(worker.abort)

        thread.started.connect(worker.work)
        thread.start()
    
    def on_stop_test_button_clicked(self):
        '''
        self.sig_abort_workers.emit()
        for thread, Worker in self.__threads:
            thread.quit()
            thread.wait()
        sys.stdout = origin_stdout
        print('Pytest Thread Abort!')
        '''

    def on_worker_done(self):
        sys.stdout = origin_stdout
        for thread, Worker in self.__threads:
            thread.quit()
            thread.wait()
        print('Pytest Thread Finished!')

    def show_info(self, line):
        self.ui.list.insertPlainText(line)
        self.ui.list.insertPlainText('\n')
        self.ui.list.show()
    

