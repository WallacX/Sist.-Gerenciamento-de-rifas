import models.model_rifas as RifasModel


class ListaRifas:
    def __init__(self, listWidget ,parent):
        self.listWidget = listWidget
        self.parent = parent
        self.listaRifas = []

        self.carregaDados()
        self.listWidget.clicked.connect(self.on_click)


    def on_click(self):
        selected_row = self.listWidget.currentRow() #linha selecionada
        rifa = self.listaRifas[selected_row]
        self.parent.insereRifa(rifa)


    def carregaDados(self):
        self.listaRifas = RifasModel.getAtivas()
        for rifa in self.listaRifas:
            self.listWidget.addItem(rifa.premio)