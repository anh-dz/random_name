from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from main import *

from . random_name import ran_name

class RAN:
    def __init__(self, widgets: ViewControl):
        global wgs
        wgs = widgets
        wgs.btn_Press.clicked.connect(self.gift_ran)
    
    def gift_ran(self):
        wgs.btn_Press.setIconSize(QtCore.QSize(64, 64))
        self.my_qtimer = QTimer()
        self.my_qtimer.start(100)
        self.my_qtimer.timeout.connect(lambda: wgs.btn_Press.setIconSize(QtCore.QSize(90, 90)))

        ls = ran_name()

        wgs.btn_Fname.setText(ls[0])
        wgs.btn_Sname.setText(ls[1])

