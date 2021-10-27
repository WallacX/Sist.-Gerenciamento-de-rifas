import models.model_rifas as RifasModel


class ListaRifas:
    def __init__(self, listWidget ,parent):
        self.listWidget = listWidget
        self.parent = parent
        self.listaRifas = []

        self.carregaDados()
        #self.listWidget.clicked.connect(self.on_click)


    def on_click(self,x):
        rifa = self.listaRifas[x]
        self.parent.insereRifa(rifa)


    def carregaDados(self):
        self.listaRifas = RifasModel.getAtivas()
        lista_combo = []
        for rifa in self.listaRifas:
            lista_combo.append(rifa.premio)
        self.listWidget.addItems(lista_combo)



    