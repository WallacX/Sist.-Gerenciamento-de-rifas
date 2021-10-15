from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from tables.table_rifas import TabelaRifas


class Criar(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/criar.ui",self)

        self.table = TabelaRifas(self)

        self.setEventos()

    def setEventos(self):
        self.criar_btn.clicked.connect(self.criarRifa)

    def criarRifa(self):
        self.table.criaTabela(int(self.qtd_numeros_line.text()))
        self.layout_principal.addWidget(self.table)

