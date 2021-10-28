from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtCore import QSize

import models.model_rifas as RifasModel



class TabelaFinalizadas:
    def __init__(self, tableWidget, parent):
        self.tableWidget = tableWidget
        self.parent = parent

        self.rifa = None

        self.listaRifas= []


        self.configTable()
        self.tableWidget.setRowCount(0)
        self.carregaDados()


    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
    
    
    def carregaDados(self):
        self.listaRifas = RifasModel.getFinalizadas()
        self.tableWidget.setRowCount(0)
        print (len(self.listaRifas))
        '''for rifa in self.listaRifas:
            self._addRow(rifa)
'''

    def delRifa(self, rifa):
        RifasModel.delRifa(rifa.id)
        self.carregaDados()



    def _addRow(self, rifa):
        self.listaRifas.append(rifa)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)


        id = QTableWidgetItem(str(rifa.id))
        premio = QTableWidgetItem(rifa.premio)
        qtd_num = QTableWidgetItem(rifa.qtd_num)
        #num_sort = QTableWidgetItem(rifa.num_sort)

        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, premio)
        self.tableWidget.setItem(rowCount, 2, qtd_num)
        #self.tableWidget.setItem(rowCount, 3, num_sort)
        self.tableWidget.setCellWidget(rowCount, 3, CustomQWidget(rifa,self))



class CustomQWidget(QWidget):
    def __init__(self, rifa, parent):
        super(CustomQWidget, self).__init__()
        self.rifa = rifa
        self.parent = parent
        self.btn = QPushButton(self)
        self.btn.setText("")
        self.btn.setIcon(QIcon("icones/deletar.png"))
        self.btn.setShortcut('Ctrl+D')
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Remover "+ str(self.rifa.premio)+"?")
        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}')
        self.btn.setIconSize(QSize(20,20))
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)


    def remover(self):
        self.parent.delRifa(self.rifa)