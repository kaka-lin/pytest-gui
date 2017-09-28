from PyQt5 import QtCore, QtGui, QtWidgets
from gui.testareabox import TestAreaBox

class Test1Tab(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super(Test1Tab, self).__init__(parent)
      
        self.test_area_box = TestAreaBox()
        self.addWidget(self.test_area_box)

        self._setup_ui()
    
    def _setup_ui(self):
        self.retranslateUi()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate