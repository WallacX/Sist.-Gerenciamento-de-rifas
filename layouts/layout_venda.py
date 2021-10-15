from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Venda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/venda.ui",self)
