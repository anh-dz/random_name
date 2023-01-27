from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from main import *


class RAN:
    def __init__(self, widgets: ViewControl):
        global wgs
        wgs = widgets
        wgs.btn_Press.clicked.connect(self.gift_ran)
    
    def gift_ran(self):
        pass