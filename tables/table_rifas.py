from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

class TabelaRifas(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 10)
        self.janela_pai = janela_pai
        headers = ["","","","","","","","","",""]
        self.setHorizontalHeaderLabels(headers)
        self.configTable()

    def criaTabela(self,qtd):
        qtd_num = qtd
        colunas = 10
        linhas = qtd_num//colunas
        if qtd_num % colunas > 0:
            linhas += 1
        num = 1
        for l in range(0, linhas):
            rowCount = self.rowCount()
            self.insertRow(rowCount)
            for c in range(0, colunas):
                i = QTableWidgetItem(str(num))
                self.setItem(rowCount, c, i)
                num += 1
                if num > qtd_num:
                    break


    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)#possivelmete vai precisar editar talvez só tirar o 's' no final de Rows
        # evento ao selecionar uma linha
        '''self.clicked.connect(self.on_click)'''



'''
    def carregaDados(self):
        self.teste()
        self.lista_clientes = ClientesModel.getClientes()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0) # reinicia a contagem de linhas add na tabela
        # adiciona os elementos na tabela
        for cliente in self.lista_clientes:
            self._addRow(cliente)

    def _addRow(self, cliente):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

        # fixa a linha e muda a coluna conforme os valores
        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        cpf = QTableWidgetItem(cliente.cpf)
        telefone = QTableWidgetItem(cliente.telefone)
        email = QTableWidgetItem(cliente.email)

        # insere os itens na tabela
        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, cpf)
        self.setItem(rowCount, 3, telefone)
        self.setItem(rowCount, 4, email)


    def on_click(self):
        #linha onde foi clicado
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        cliente = ClientesModel.getCliente(id)
        # insere os valores nos campos na janela principal
        self.janela_pai.insereCliente(cliente)
'''