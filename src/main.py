import os
import sys
from PyQt5.QtCore import QCoreApplication, QUrl, Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

from src.manage_threads import ManageThreads
from src.model import Model

def run(app):
    dir_name = os.path.dirname(__file__)
    os.environ['QML_IMPORT_PATH'] = os.path.join(dir_name, 'resources')
    os.environ['QML2_IMPORT_PATH'] = os.path.join(dir_name, 'resources')

    #QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    # Create the application instance.
    #app = QGuiApplication(sys.argv)

    # Create QML engine
    engine = QQmlApplicationEngine()
    context = engine.rootContext()

    # Testor
    manage = ManageThreads()
    context.setContextProperty("manage", manage)

    # Model
    TestorModel = Model()
    manage.runtimeSig.connect(TestorModel.addData)
    context.setContextProperty("TestorModel", TestorModel)

    engine.load(QUrl('src/resources/main.qml'))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    run(app)
