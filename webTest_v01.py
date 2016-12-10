import sys
import PySide
from PySide.QtCore import *
from PySide.QtGui import *

qt_app = QApplication(sys.argv)

class helloWorldApp(QLabel):
    def __init__(self):
        QLabel.__init__(self, 'hello world')

        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello fuckin\' world!')

    def run(self):
        self.show()
        qt_app.exec_()

helloWorldApp().run()