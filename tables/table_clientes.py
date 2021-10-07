from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem,  QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect
import models.model_clientes as ClientesModel

class TabelaClientes(QTableWidget):
    def __init__(self, tableWidget, parent):

        self.tableWidget = tableWidget
        self.parent = parent

        self.configTable()
        self.carregaDados()
        self.tableWidget.setRowCount(0)


    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.clicked.connect(self.on_click)


    def carregaDados(self):
        self.lista_clientes = ClientesModel.getClientes()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0) # reinicia a contagem de linhas add na tabela
        # adiciona os elementos na tabela
        for cliente in self.lista_clientes:
            self._addRow(cliente)


    def _addRow(self, cliente):#ver o que é esse cliente/item q tá passando
        self.listaItens.append(cliente)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        
        id = QTableWidgetItem(str(cliente.id))
        nome= QTableWidgetItem(cliente.nome)
        cpf = QTableWidgetItem(cliente.cpf)
        telefone = QTableWidgetItem(cliente.telefone)
        email = QTableWidgetItem(cliente.email)

        '''id = x[0]
        nome = x[1]
        cpf = x[2]
        telefone = x[3]
        email = x[4]
        cliente = Cliente(id, nome, cpf, telefone, email)
        lista_clientes.append(cliente)'''

        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, nome)
        self.tableWidget.setItem(rowCount, 2, cpf)
        self.tableWidget.setItem(rowCount, 3, telefone)
        self.tableWidget.setItem(rowCount, 4, email)
        self.tableWidget.setCellWidget(rowCount, 5, CustomQWidget(cliente,self))



    def on_click(self):
        selected_row = self.tableWidget.currentRow()
        id = self.item(selected_row, 0).text()
        cliente = ClientesModel.getCliente(id)

        self.janela_pai.insereCliente(cliente)
        self.itemAtual = self.listaItens[selected_row]
        self.parent.btn_remover_item.setEnabled(True)



    def addCliente(self, cliente):
        ClientesModel.addCliente(cliente)
        self.carregaDados()

    def editCliente(self, cliente):
        ClientesModel.editCliente(cliente)
        self.carregaDados()

    def delCliente(self, cliente):
        ClientesModel.delCliente(cliente.id)
        self.carregaDados()






class CustomQWidget(QWidget):
    def __init__(self, item, parent):
        super(CustomQWidget, self).__init__()
        self.item = item
        self.parent = parent
        self.btn = QPushButton(self)
        self.btn.setText("")
        self.btn.setIcon(QIcon("icones/deletar.png"))
        self.btn.setShortcut('Ctrl+D')
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Remover "+ str(self.item.cliente.nome)+"?")
        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}')
        self.btn.setIconSize(QSize(20,20))
        

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def remover(self):
        self.parent.itemAtual = self.item
        self.parent.limparSelecionado()