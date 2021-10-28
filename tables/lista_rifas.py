import models.model_rifas as RifasModel


class ListaRifas:
    def __init__(self, listWidget ,parent):
        self.listWidget = listWidget
        self.parent = parent
        self.listaRifas = []

        self.carregaDados()


    def on_click(self,x):
        print([x])
        rifa = self.listaRifas[x-1]
        self.parent.insereRifa(rifa)
        self.parent.verifica()


    def carregaDados(self):
        self.listWidget.clear()
        self.listaRifas = RifasModel.getAtivas()
        lista_combo = []
        lista_combo.append("SELECIONE UMA RIFA")
        for rifa in self.listaRifas:
            lista_combo.append(rifa.premio)
        self.listWidget.addItems(lista_combo)