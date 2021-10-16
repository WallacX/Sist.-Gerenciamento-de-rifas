from PyQt5.QtWidgets import QHeaderView, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import models.model_rifas as RifasModel


class ListaRifas:
    def __init__(self, listWidget ,parent):
        self.listWidget = listWidget
        self.parent = parent

        self.configList()


        self.carregaDados()

    def configList(self):
        self.listWidget.verticalHeader().setVisible(False)
        self.listWidget.horizontalHeader().setStretchLastSection(False)
        self.listWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.listWidget.setEditTriggers(QListWidget.NoEditTriggers)
        self.listWidget.setSelectionBehavior(QListWidget.SelectRows)
        #self.tableWidget.clicked.connect(self.on_click)

    
    def carregaDados(self):
        self.listWidget.addItem(RifasModel.getAtivas())