from PyQt5.QtWidgets import QHeaderView, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import models.model_rifas as RifasModel


class ListaRifas:
    def __init__(self, listWidget ,parent):
        self.listWidget = listWidget
        self.parent = parent


        self.carregaDados()

    def carregaDados(self):
        lista_rifa = RifasModel.getAtivas()
        for rifa in lista_rifa:
            self.listWidget.addItem(rifa)