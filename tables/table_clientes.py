from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtCore import QSize

import models.model_clientes as ClientesModel
import layouts.layout_clientes as ClientesLayout


class TabelaClientes:
    def __init__(self, tableWidget ,parent):
        self.tableWidget = tableWidget
        self.parent = parent

        self.cliente = None

        self.listaClientes= []


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
        self.tableWidget.clicked.connect(self.on_click)
        
    def carregaDados(self):
        self.lista_clientes = ClientesModel.getClientes()
        self.tableWidget.setRowCount(0)
        for cliente in self.lista_clientes:
            self._addRow(cliente)
    def addCliente(self, cliente):
        ClientesModel.addCliente(cliente)
        self.carregaDados()
    def editCliente(self, cliente):
        ClientesModel.editCliente(cliente)
        self.carregaDados()

    def delCliente(self, cliente):
        
        ClientesModel.delCliente(cliente.id)

        self.carregaDados()

    def limparClientes(self):
        
        self.parent.excluir_btn.setEnabled(False)
        self.parent.limpar_btn.setEnabled(False)


    def on_click(self):
        selected_row = self.tableWidget.currentRow() #linha selecionada
        id = self.tableWidget.item(selected_row, 0).text()
        cliente = ClientesModel.getCliente(id)
        self.parent.insereCliente(cliente)
        self.clienteAtual = self.listaClientes[selected_row]


    def _addRow(self, cliente):
        self.listaClientes.append(cliente)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)


        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        cpf = QTableWidgetItem(cliente.cpf)
        telefone = QTableWidgetItem(cliente.telefone)
        email = QTableWidgetItem(cliente.email)
        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, nome)
        self.tableWidget.setItem(rowCount, 2, cpf)
        self.tableWidget.setItem(rowCount, 3, telefone)
        self.tableWidget.setItem(rowCount, 4, email)
        self.tableWidget.setCellWidget(rowCount, 5, CustomQWidget(cliente,self))


    def limparSelecionado(self):
        self.listaClientes.remove(self.clienteAtual)
        novaLista = self.listaClientes
        self.limparClientes()
        self.parent.limpar_btn.setEnabled(True)
        for x in novaLista:
            self._addRow(x)


            
class CustomQWidget(QWidget):
    def __init__(self, cliente, parent):
        super(CustomQWidget, self).__init__()
        self.cliente = cliente
        self.parent = parent
        self.btn = QPushButton(self)
        self.btn.setText("")
        self.btn.setIcon(QIcon("icones/deletar.png"))
        self.btn.setShortcut('Ctrl+D')
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Remover "+ str(self.cliente.nome)+"?")
        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}')
        self.btn.setIconSize(QSize(20,20))
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)


    def remover(self):
        self.parent.delCliente(self.cliente)