from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import pytest
from _pytest.runner import runtestprotocol
from _pytest.main import EXIT_OK, EXIT_TESTSFAILED, EXIT_INTERRUPTED, \
    EXIT_USAGEERROR, EXIT_NOTESTSCOLLECTED

import time

class kakaPlugin(QObject):
    runtimeSig = pyqtSignal(str, str, arguments=['item', 'result'])

    def __init__(self, parent=None):
        super(kakaPlugin, self).__init__(parent)

        self.item_collected = []
        self.results = {}

    def pytest_collection_modifyitems(self, items):
        for item in items:
            self.item_collected.append(item.nodeid)

    '''
    @pytest.hookimpl(trylast=True)
    def pytest_sessionstart(self, session):
        print("********************* start *********************")  
        '''  

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_protocol(self, item, nextitem):
        reports = runtestprotocol(item, nextitem=nextitem)
        for report in reports:
            if report.when == 'call':
                self.results[item.name] = report.outcome
                print('%s --- %s' % (item.name, report.outcome))
                yield self.runtimeSig.emit(item.name, report.outcome)
        
        '''
    def pytest_sessionfinish(self, exitstatus):
        print("********************* finish *********************")
        if exitstatus == EXIT_OK:
            print('TEST PASS!!!')
        
        if exitstatus == EXIT_TESTSFAILED:
            print('TEST FAILED!!!')
            '''
            
class TestorThread(QObject):
    runtimeSig = pyqtSignal(str, str, arguments=['item', 'result'])
    testDone = pyqtSignal()

    def __init__(self, path=None, parent=None):
        super(TestorThread, self).__init__(parent)

        self.path = path

        self.my_plugin = kakaPlugin()
        self.my_plugin.runtimeSig.connect(self.runtimeSig)
    
    @pyqtSlot()
    def run(self):
        pytest.main(['-p', 'no:terminal', self.path], plugins=[self.my_plugin])
        self.testDone.emit()

    '''
    @pyqtSlot()
    def test(self):
        my_plugin = kakaPlugin()
        pytest.main(['--collect-only', self.path], plugins=[my_plugin])

        for nodeid in my_plugin.collected:
            print(nodeid)
    '''
    