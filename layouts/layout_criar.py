from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QDate

from componentes.rifa import Rifa
import models.model_rifas as RifasModel



class CriarRifa(QWidget):
    def __init__(self,parent):
        super(). __init__()
        uic.loadUi("ui/criar.ui",self)

        self.parent = parent


        self.verifica()
        self.setEventos()


    def setEventos(self):
        self.premio_line.textEdited.connect(self.verifica)

        self.criar_btn.clicked.connect(self.criarRifa)

    def criarRifa(self):
        novaRifa = self.getRifa()
        if novaRifa != None:
            RifasModel.addRifa(novaRifa)

            self.close()
            self.parent.carregaDados()

    def getRifa(self):
        if(self.premio_line.text() != ""):
            return Rifa(-1,self.premio_line.text(), int(self.qtd_num_spin.text()) ,"ATIVA")
        else:
            return None




    def verifica(self):
        if(self.premio_line.text() != ""):
            self.criar_btn.setEnabled(True)
        else:
            self.criar_btn.setEnabled(False)