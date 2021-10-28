from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QDate

from tables.lista_rifas import ListaRifas
from layouts.layout_criar import CriarRifa
from tables.table_rifas import TabelaRifas
from componentes.venda import Venda

import models.model_clientes as ClientesModel
import models.model_rifas as RifasModel



class NovaVenda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/venda.ui",self)

        self.rifaAtual = None
        self.clienteAtual= None
        
        self.tabelaRifas = TabelaRifas(self.tableWidget, self)
        self.listaRifas= ListaRifas(self.combo_rifas, self)


        qtd_validator = QRegExpValidator(QRegExp('^[1-9]{1}[0-9]{3}$'), self.numero_line)
        self.numero_line.setValidator(qtd_validator)


        self.carregaDadosCliente()
        self.setEventos()


    def setEventos(self):
        self.compra_btn.setEnabled(False)
        self.numero_line.textEdited.connect(self.verifica)
        self.combo_clientes.currentIndexChanged.connect(self.index_changed_cliente)
        self.combo_rifas.currentIndexChanged.connect(self.listaRifas.on_click)
        self.novo_btn.clicked.connect(self.redirecionar)
        self.compra_btn.clicked.connect(self.comprar)
        self.finaliza_btn.clicked.connect(self.finalizar)

    def atualiza(self):
        self.combo_rifas.currentIndexChanged.connect(self.listaRifas.carregaDados)

    def redirecionar(self):
        self.w = CriarRifa(self)
        self.w.show()

    def insereRifa(self,rifa):
        self.tabelaRifas.criaTabela(rifa.qtd_num,rifa.id)
        self.rifaAtual = rifa


    def index_changed_cliente(self, x):
        if x != 0:
            self.clienteAtual = self.lista_clientes[x-1]#acho q dps vai ter q tirar esse -1 (dps q eu recriar a tabela)
        else:
            self.clienteAtual =  None



    def carregaDadosCliente(self):
        self.lista_clientes = ClientesModel.getClientes()
        lista_combo = []
        for cliente in self.lista_clientes:
            lista_combo.append(cliente.nome)
        self.combo_clientes.addItems(lista_combo)


    def comprar(self):
        if self.clienteAtual != None:
            rifa = self.rifaAtual
            id_rifa = self.rifaAtual.id
            id_cliente = self.clienteAtual.id
            numero = int(self.numero_line.text())

            novaVenda = Venda(-1, id_rifa, id_cliente, numero)
            RifasModel.addVenda(novaVenda)
            self.insereRifa(rifa)
            self.verifica()


    def finalizar(self):
        return None



    def verifica(self):


        if self.rifaAtual == None:
            self.avisos_label.setText("Selecione uma rifa")
            self.compra_btn.setEnabled(False)
        elif self.clienteAtual == None:
            self.avisos_label.setText("Selecione um cliente")
            self.compra_btn.setEnabled(False)
        elif self.numero_line.text() != (""):
            self.avisos_label.setText("Digite um número")


        if self.rifaAtual != None  and  self.numero_line.text() != (""):
            if int(self.numero_line.text()) > self.rifaAtual.qtd_num:
                self.avisos_label.setText("O número digitado é maior que a quantidade de números da tabela")
                self.compra_btn.setEnabled(False)

            elif self.rifaAtual != None and self.clienteAtual != None and self.numero_line.text() != (""):
                numero = int(self.numero_line.text())
                lista = RifasModel.verificaVenda(self.rifaAtual.id)

                for x in lista:
                    if numero == x[0] or self.numero_line.text() == "0":
                        self.avisos_label.setText("Este número já foi comprado")
                        self.compra_btn.setEnabled(False)


                    else:
                        self.avisos_label.setText("")
                        self.compra_btn.setEnabled(True)