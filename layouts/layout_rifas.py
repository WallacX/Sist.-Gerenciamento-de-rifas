from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from tables.table_rifas import TabelaRifas

#tabela fica em stand-by até eu clicar no botão

class Rifas(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/rifas.ui",self)
        #self.qtd_numeros_line.setText("15")

        self.table = TabelaRifas(self)

        #self.layout_principal.addWidget(self.table)

        self.setEventos()

    def setEventos(self):
        self.criar_btn.clicked.connect(self.criarRifa)

    def criarRifa(self):
        #chama a funcao que cria a tabela passando o texto da linha
        self.table.criaTabela(int(self.qtd_numeros_line.text()))
        self.layout_principal.addWidget(self.table)

