from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from tables.table_clientes import TabelaClientes
from componentes.cliente import Cliente



class PerfilClientes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/clientes.ui",self)

        self.clienteAtual = None
        self.setEventos()
        self.tabelaClientes = TabelaClientes(self.tableWidget, self)


    def setEventos(self):
        self.novo_btn.clicked.connect(self.salvarCliente)
        self.limpar_btn.clicked.connect(self.limpaCampos)
        self.excluir_btn.clicked.connect(self.excluirItem)


    def salvarCliente(self):

        novoCliente = self.getCliente()
        if novoCliente != None:
            if self.clienteAtual == None:
                self.tabelaClientes.addCliente(novoCliente)
            else:
                novoCliente.id = self.clienteAtual.id
                self.tabelaClientes.editCliente(novoCliente)

            self.limpaCampos()


    def getCliente(self):
        if((self.nome_line.text() != "") and (self.cpf_line.text() != "")) and (self.telefone_line.text() != ""):
            return Cliente(2, self.nome_line.text(), self.cpf_line.text(), self.telefone_line.text(), self.email_line.text())
        return None


    def limpaCampos(self):
        self.clienteAtual = None
        self.nome_line.setText("")
        self.cpf_line.setText("")
        self.telefone_line.setText("")
        self.email_line.setText("")

        self.novo_btn.setText("Novo Cliente")
        self.excluir_btn.setEnabled(False)
        self.limpar_btn.setEnabled(False)



    def insereCliente(self, cliente):
        self.clienteAtual = cliente
        self.nome_line.setText(cliente.nome)
        self.cpf_line.setText(cliente.cpf)
        self.telefone_line.setText(cliente.telefone)
        self.email_line.setText(cliente.email)
        self.novo_btn.setText("Atualizar")
        self.excluir_btn.setEnabled(True)

    def excluirItem(self):
        self.tabelaClientes.delCliente(self.clienteAtual)
        self.limpaCampos()