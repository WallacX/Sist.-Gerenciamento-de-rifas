from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from tables.table_rifas import TabelaRifas
from componentes.rifa import Rifa
import models.model_rifas as RifasModel

class CriarRifa(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/criar.ui",self)

        self.table = TabelaRifas(self)
        self.setEventos()

    def setEventos(self):
        self.criar_btn.clicked.connect(self.criarRifa)

    def criarRifa(self):
        novaRifa = self.getRifa()
        if novaRifa != None:
            RifasModel.addRifa(novaRifa)

            #self.layout_principal.addWidget(self.table)
            self.limpaCampos()

    def getRifa(self):
        if((self.premio_line.text() != "") and (self.qtd_num_line.text() != "")):
            return Rifa(-1,self.premio_line.text(), int(self.qtd_num_line.text()) ,"ATIVA")
        return None

    def limpaCampos(self):
        self.premio_line.setText("")
        self.qtd_num_line.setText("")