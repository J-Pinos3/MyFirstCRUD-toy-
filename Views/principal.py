import sys
import os
#myDir = os.getcwd()
myDir = "C:/Users/Usuario/Desktop/CRUD_python_mysql"
sys.path.append(myDir)

from Controllers.PrincipalController import PrincipalController
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.createProduct import Ui_CreateProduct

class Ui_Principal(object):

    def __init__(self):
        self.principal_controller = PrincipalController(self)


    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(748, 600)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.table_product = QtWidgets.QTableWidget(self.centralwidget)
        self.table_product.setGeometry(QtCore.QRect(160, 70, 431, 351))
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        self.btn_listar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listar.setGeometry(QtCore.QRect(50, 490, 75, 24))
        self.btn_listar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_listar.setStyleSheet("background-color: rgb(28, 255, 187);\n"
"selection-color: rgb(28, 255, 187);\n"
"border-color: rgb(0, 0, 255);")
        self.btn_listar.setObjectName("btn_listar")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(180, 490, 75, 24))
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update.setStyleSheet("background-color: rgb(28, 255, 187);\n"
"selection-color: rgb(28, 255, 187);\n"
"border-color: rgb(0, 0, 255);")
        self.btn_update.setObjectName("btn_update")
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(310, 490, 75, 24))
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setStyleSheet("background-color: rgb(28, 255, 187);\n"
"selection-color: rgb(28, 255, 187);\n"
"border-color: rgb(0, 0, 255);")
        self.btn_create.setObjectName("btn_create")
        self.btn_read = QtWidgets.QPushButton(self.centralwidget)
        self.btn_read.setGeometry(QtCore.QRect(440, 490, 91, 24))
        self.btn_read.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_read.setStyleSheet("background-color: rgb(28, 255, 187);\n"
"selection-color: rgb(28, 255, 187);\n"
"border-color: rgb(0, 0, 255);")
        self.btn_read.setObjectName("btn_read")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(590, 490, 75, 24))
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet("background-color: rgb(255, 144, 150);\n"
"selection-color: rgb(255, 144, 150);\n"
"border-color: rgb(255, 0, 34);")
        self.btn_delete.setObjectName("btn_delete")
        Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)
        #---------------------------------------EVENTS---------------------------------------
        self.l = self.btn_listar.clicked.connect(lambda: self.principal_controller.listProducts())
        self.c = self.btn_create.clicked.connect(lambda: self.principal_controller.openCreate(Ui_CreateProduct))
        self.r = self.btn_read.clicked.connect(lambda: self.principal_controller.showProduct())
        self.u = self.btn_update.clicked.connect(lambda: self.principal_controller.updateProducs())
        self.d = self.btn_delete.clicked.connect(lambda: self.principal_controller.deleteProducs())
        #---------------------------------------END EVENTS---------------------------------------
    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "MainWindow"))
        self.label.setText(_translate("Principal", "VENTANA PRINCIPAL"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "CÓDIGO"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "NOMBRE"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "PRECIO"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "CATEGORÍA"))
        self.btn_listar.setText(_translate("Principal", "LISTAR"))
        self.btn_update.setText(_translate("Principal", "ACTUALIZAR"))
        self.btn_create.setText(_translate("Principal", "CREAR"))
        self.btn_read.setText(_translate("Principal", "SELECCIONAR"))
        self.btn_delete.setText(_translate("Principal", "ELIMINAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
