from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from tables.lista_rifas import ListaRifas
from layouts.layout_criar import CriarRifa
import models.model_clientes as ClientesModel


from tables.table_rifas import TabelaRifas
from componentes.rifa import Rifa
import models.model_rifas as RifasModel

class CriarRifa(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/criar.ui",self)

        self.table = TabelaRifas(self)
        self.setEventos()

    def setEventos(self):
        self.criar_btn.clicked.connect(self.criarRifa)

    def criarRifa(self):
        novaRifa = self.getRifa()
        if novaRifa != None:
            RifasModel.addRifa(novaRifa)
            self.limpaCampos()

    def getRifa(self):
        if((self.premio_line.text() != "") and (self.qtd_num_line.text() != "")):
            return Rifa(-1,self.premio_line.text(), int(self.qtd_num_line.text()) ,"ATIVA")
        return None

    def limpaCampos(self):
        self.premio_line.setText("")
        self.qtd_num_line.setText("")





class Venda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/venda.ui",self)

        self.rifaAtual = None

        self.listaVendas = ListaRifas(self.listWidget, self)
        self.tabelaVenda = TabelaRifas(self)
        self.layout_principal.addWidget(self.tabelaVenda)
        self.carregaDadosCliente()
        self.setEventos()

    def setEventos(self):
        self.novo_btn.clicked.connect(self.redirecionar)


    def redirecionar(self):
        self.w = CriarRifa()
        self.w.show()


    def insereRifa(self,rifa):
        self.rifaAtual = rifa
        self.premio_line.setText(rifa.premio)



    def carregaDadosCliente(self):
        self.lista_clientes = ClientesModel.getClientes()
        lista_combo = []
        for cliente in self.lista_clientes:
            lista_combo.append(cliente.nome)
        self.combo_clientes.addItems(lista_combo)







