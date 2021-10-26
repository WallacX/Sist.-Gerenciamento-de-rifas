from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


from componentes.rifa import Rifa
import models.model_rifas as RifasModel



class CriarRifa(QWidget):
    def __init__(self,parent):
        super(). __init__()
        uic.loadUi("ui/criar.ui",self)

        self.parent = parent

        self.setEventos()

    def setEventos(self):
        self.criar_btn.clicked.connect(self.criarRifa)

    def criarRifa(self):
        novaRifa = self.getRifa()
        if novaRifa != None:
            RifasModel.addRifa(novaRifa)


            self.limpaCampos()
            self.close()
            self.parent.carregaDados()


    def getRifa(self):
        if((self.premio_line.text() != "") and (self.qtd_num_line.text() != "")):
            return Rifa(-1,self.premio_line.text(), int(self.qtd_num_line.text()) ,"ATIVA")
        return None

    def limpaCampos(self):
        self.premio_line.setText("")
        self.qtd_num_line.setText("")