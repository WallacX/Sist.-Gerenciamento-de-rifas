import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem, QApplication
from PyQt5 import uic

from qt_material import apply_stylesheet

from layouts.layout_clientes import PerfilClientes
from layouts.layout_venda import NovaVenda
from layouts.layout_finalizadas import RifasFinalizadas
#linha 14 menu.ui

#verificação se o numero já foi vendido/não poder vender um numero já vendido
#limitar o numero digitado ao maximo de numeros na rifa


#alterar a interface com relação aos botões na ui.clientes  na ui.vendas


#Botão estou com sorte (te diz um numero aleatorio ainda nao comprado)?
#fazer um on_click da tabela de rifas?

#acho q na hr da verificaçao do n vai ter q passar o numero da rifa, adicionar todos 
#os numeros vendidos dessa rifa numa lista e ver se tem algum numero igual ao digitado

#criar a parte de escolher o numero sorteado

#apagar as rifas
#definir tamanho criar.ui
class CustomQWidget(QWidget):
    def __init__(self, icon, text, parent= None):
        super(CustomQWidget, self).__init__(parent)

        label_icon = QLabel(icon)
        label_text = QLabel(text)

        layout = QHBoxLayout()
        layout.addWidget(label_icon)
        layout.addWidget(label_text)
        layout.addWidget(label_icon)

        self.setLayout(layout)


class JanelaPrincipal(QMainWindow):
    def __init__(self) :
        super().__init__()
        uic.loadUi("ui/menu.ui", self)


        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+","Rifas Ativas")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(0,item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+","Clientes")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1,item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+","Rifas Finalizadas")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1,item)
        self.listWidget.setItemWidget(item, item_widget)


        self.listWidget.setCurrentRow(0)
        self.carregaJanelas()
        self.listWidget.currentRowChanged.connect(self.display)


    def carregaJanelas(self):
        self.stackedWidget.addWidget(NovaVenda())
        self.stackedWidget.addWidget(PerfilClientes())
        self.stackedWidget.addWidget(RifasFinalizadas())



    def display(self, index):
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)



app = QApplication(sys.argv)
apply_stylesheet(app, theme = 'dark_teal.xml')

window = JanelaPrincipal()
window.show()

app.exec()