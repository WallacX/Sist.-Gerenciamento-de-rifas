from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from tables.lista_rifas import ListaRifas
from layouts.layout_criar import CriarRifa



class Venda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/venda.ui",self)

        
        self.setEventos()

    def setEventos(self):
        self.novo_btn.clicked.connect(self.redirecionar)
        self.tabelaClientes = ListaRifas(self.listWidget, self)

    def redirecionar(self):
        self.w = CriarRifa()
        self.w.show()