from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem
from PyQt5 import uic

#from layouts.clientes import PerfilClientes


class CustomQWidget(QWidget):
    def __init__(self, icon, text, parent= None):
        super(CustomQWidget).__init__(parent)

    label_icon = QLabel(icon)
    label_text = QLabel(text)

    layout = QHBoxLayout()
    layout.addWidget(label_icon)
    layout.addWidget(label_text)
    layout.addWidget(label_icon)



class JanelaPrincipal(QMainWindow):
    def __init__(self) :
        super().__init__()
        uic.loadUi("ui/menu.ui", self)