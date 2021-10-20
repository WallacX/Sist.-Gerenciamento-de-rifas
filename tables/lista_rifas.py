from PyQt5.QtWidgets import QHeaderView, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import models.model_rifas as RifasModel


class ListaRifas:
    def __init__(self, listWidget ,parent):
        self.listWidget = listWidget
        self.parent = parent
        #self.listaRifas = []

        self.carregaDados()
        self.listWidget.clicked.connect(self.on_click)

    def on_click(self):
        selected_row = self.listWidget.currentRow() #linha selecionada
        premio = self.listWidget.item(selected_row).text()
        rifa = RifasModel.getRifa(premio)
        
        self.parent.insereRifa(rifa)
        #self.rifaAtual = self.listaRifas[selected_row]

    def carregaDados(self):
        lista_rifa = RifasModel.getAtivas()
        for rifa in lista_rifa:
            self.listWidget.addItem(rifa)