import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem, QApplication
from PyQt5 import uic

from qt_material import apply_stylesheet

from layouts.layout_clientes import PerfilClientes
from layouts.layout_venda import Venda
from layouts.layout_criar import CriarRifa

#Exibir a lista de rifas ativas



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




        self.listWidget.setCurrentRow(0)
        self.carregaJanelas()
        self.listWidget.currentRowChanged.connect(self.display)


    def carregaJanelas(self):
        self.stackedWidget.addWidget(Venda())
        self.stackedWidget.addWidget(PerfilClientes())




    def display(self, index):
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)



app = QApplication(sys.argv)
apply_stylesheet(app, theme = 'dark_teal.xml')

window = JanelaPrincipal()
window.show()
app.exec()


