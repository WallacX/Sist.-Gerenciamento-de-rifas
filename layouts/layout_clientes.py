from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from tables.table_clientes import TabelaClientes
from componentes.cliente import Cliente


class PerfilClientes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/clientes.ui", self)


        self.lista_clientes = []#?????????????
        self.clienteAtual = None
        self.setEventos()



        self.tabelaClientes = TabelaClientes(self.tableWidget, self)
        




    # define os eventos de todos os botões
    def setEventos(self):
        self.novo_btn.clicked.connect(self.salvarCliente)
        self.limpar_btn.clicked.connect(self.limpaCampos)
        self.excluir_btn.clicked.connect(self.excluirItem)






    def salvarCliente(self):
        # adiciona os campos na tabela
        novoCliente = self.getCliente()
        # verifica os campos vazios
        if novoCliente != None:
            # é um novo contato
            if self.clienteAtual == None:
                # manda add no banco de dados
                self.table.addCliente(novoCliente)
            else:
                # manda editar no bando de dados
                novoCliente.id = self.clienteAtual.id
                self.table.editCliente(novoCliente)
            # limpa os campos
            self.limpaCampos()

    # pega as informações digitadas nos campos do Contato
    def getCliente(self):
        if((self.nome_line.text() != "") and (self.cpf_line.text() != "")) and (self.telefone_line.text() != "") and (self.endereco_line.text() != ""):
            return Cliente(-1, self.nome_line.text(), self.cpf_line.text(), self.telefone_line.text(), self.email_line.text(), self.endereco_line.text())
        return None

    # limpa os campos e restaura os valores originais dos componentes
    def limpaCampos(self):
        self.clienteAtual = None
        self.nome_line.setText("")
        self.cpf_line.setText("")
        self.telefone_line.setText("")
        self.email_line.setText("")
        self.endereco_line.setText("")

        self.novoButton.setText("Novo")
        self.excluirButton.setEnabled(False)

    # utilizado para preencher os campos na janela principal
    def insereCliente(self, cliente):
        self.clienteAtual = cliente
        self.nome_line.setText(cliente.nome)
        self.cpf_line.setText(cliente.cpf)
        self.telefone_line.setText(cliente.telefone)
        self.email_line.setText(cliente.email)
        self.endereco_line.setText(cliente.endereco)

        # muda o nome do botão para atualizar (já que existe o Contato)
        self.novoButton.setText("Atualizar")
        self.excluirButton.setEnabled(True)

    def excluirItem(self):
        self.table.delCliente(self.clienteAtual)
        # limpa os campos
        self.limpaCampos()