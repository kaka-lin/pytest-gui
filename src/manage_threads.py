import os

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from src.testor_thread import TestorThread

class ManageThreads(QObject):
    runtimeSig = pyqtSignal(str, str, arguments=['item', 'result'])
    finalResultSig = pyqtSignal(str, arguments=['final_result'])

    def __init__(self, parent=None):
        super(ManageThreads, self).__init__(parent)

        self.__threads = None
        self.__thread_maps = {}

    
    @pyqtSlot(str)
    def runTest(self, path):
        pwd = os.getcwd()
        path = pwd + '/' + path

        self.__threads = []
        worker = TestorThread(path)
        thread = QtCore.QThread(self)
        self.__threads.append((thread, worker))
        self.__thread_maps['runTest'] = self.__threads
        worker.moveToThread(thread)

        worker.runtimeSig.connect(self.runtimeSig)
        worker.finalResultSig.connect(self.finalResultSig)
        worker.testDone.connect(self.testDone)

        thread.started.connect(worker.run)
        thread.start()

    @pyqtSlot()
    def testDone(self):
        for key, value in self.__thread_maps.items():
            if key == 'runTest':
                for thread, worker in value:
                    thread.quit()
                    thread.wait()
