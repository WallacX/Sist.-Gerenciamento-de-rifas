from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from tables.table_finalizadas import TabelaFinalizadas
from componentes.rifa import Rifa
import models.model_rifas as RifasModel

from tables.lista_rifas import ListaRifas

class RifasFinalizadas(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/finalizadas.ui",self)

        
        self.rifaAtual = None

        self.tabelaRifas = TabelaFinalizadas(self.tableWidget, self)