from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from view.tm import *
from control.tmcontrol import *

import sys

class ViewControl(Ui_MainWindow):
    def __init__(self):
        super().__init__()

class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

app = QApplication(sys.argv)
mainwindows = MainApp()

def main():
    widgets = ViewControl()
    widgets.setupUi(mainwindows)

    model_obj = RAN(widgets)
    mainwindows.show()
    app.exec()

if __name__ == '__main__':
    main()
