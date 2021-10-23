from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

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
        self.id_cliente = None
        
        self.listaRifas= ListaRifas(self.listWidget, self)
        self.tabelaRifas = TabelaRifas(self)
        self.layout_principal.addWidget(self.tabelaRifas)
        self.carregaDadosCliente()
        self.setEventos()


    def setEventos(self):
        self.combo_clientes.currentIndexChanged.connect(self.index_changed_cliente)
        self.novo_btn.clicked.connect(self.redirecionar)
        self.compra_btn.clicked.connect(self.comprar)
        #self.finaliza_btn.clicked.connect(self.finalizar)


    def redirecionar(self):
        self.w = CriarRifa()
        self.w.show()

    def insereRifa(self,rifa):
        self.tabelaRifas.setRowCount(0)
        self.premio_line.setText(rifa.premio)
        self.tabelaRifas.criaTabela(rifa.qtd_num,rifa.id)
        self.rifaAtual = rifa


    def index_changed_cliente(self, x):
        self.clienteAtual = self.lista_clientes[x]
        self.id_cliente = self.lista_clientes[x].id


    def carregaDadosCliente(self):
        self.lista_clientes = ClientesModel.getClientes()
        lista_combo = []
        for cliente in self.lista_clientes:
            lista_combo.append(cliente.nome)
        self.combo_clientes.addItems(lista_combo)



    def comprar(self):
        id_rifa = self.rifaAtual.id
        id_cliente = self.id_cliente
        numero = int(self.numero_line.text())

        novaVenda = Venda(-1, id_rifa, id_cliente, numero)
        RifasModel.addVenda(novaVenda)

        #self.limparItens()
