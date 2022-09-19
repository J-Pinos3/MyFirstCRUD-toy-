import sys
import os
#myDir = os.getcwd()
myDir = "C:/Users/Usuario/Desktop/CRUD_python_mysql"
sys.path.append(myDir)

from Controllers.CreateProductController import CreateProductController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateProduct(object):

    def __init__(self):
        self.create_product_controller = CreateProductController(self)


    def setupUi(self, CreateProduct):
        CreateProduct.setObjectName("CreateProduct")
        CreateProduct.resize(467, 383)
        self.label = QtWidgets.QLabel(CreateProduct)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CreateProduct)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CreateProduct)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CreateProduct)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(CreateProduct)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.input_cod = QtWidgets.QLineEdit(CreateProduct)
        self.input_cod.setGeometry(QtCore.QRect(160, 110, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_cod.setFont(font)
        self.input_cod.setObjectName("input_cod")
        self.input_name = QtWidgets.QLineEdit(CreateProduct)
        self.input_name.setGeometry(QtCore.QRect(160, 160, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_name.setFont(font)
        self.input_name.setObjectName("input_name")
        self.input_price = QtWidgets.QLineEdit(CreateProduct)
        self.input_price.setGeometry(QtCore.QRect(160, 210, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_price.setFont(font)
        self.input_price.setObjectName("input_price")
        self.input_category = QtWidgets.QLineEdit(CreateProduct)
        self.input_category.setGeometry(QtCore.QRect(160, 260, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_category.setFont(font)
        self.input_category.setObjectName("input_category")
        self.btn_create = QtWidgets.QPushButton(CreateProduct)
        self.btn_create.setGeometry(QtCore.QRect(180, 310, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_create.setFont(font)
        self.btn_create.setStyleSheet("background-color: rgb(28, 255, 187);\n"
"selection-color: rgb(0, 255, 127);")
        self.btn_create.setObjectName("btn_create")

        self.retranslateUi(CreateProduct)
        QtCore.QMetaObject.connectSlotsByName(CreateProduct)

        #---------------------------------------EVENTS---------------------------------------
        self.x=self.btn_create.clicked.connect(lambda: self.create_product_controller.createProduct(self.input_cod.text(), self.input_name.text(), self.input_price.text(), self.input_category.text(), CreateProduct))

        #---------------------------------------END EVENTS---------------------------------------

    def retranslateUi(self, CreateProduct):
        _translate = QtCore.QCoreApplication.translate
        CreateProduct.setWindowTitle(_translate("CreateProduct", "Form"))
        self.label.setText(_translate("CreateProduct", "<html><head/><body><p><span style=\" font-size:22pt;\">AGREGAR UN NUEVO PRODUCTO</span></p></body></html>"))
        self.label_2.setText(_translate("CreateProduct", "Código:"))
        self.label_3.setText(_translate("CreateProduct", "Nombre:"))
        self.label_4.setText(_translate("CreateProduct", "Precio:"))
        self.label_5.setText(_translate("CreateProduct", "Categoría:"))
        self.input_cod.setPlaceholderText(_translate("CreateProduct", "código"))
        self.input_name.setPlaceholderText(_translate("CreateProduct", "nombre"))
        self.input_price.setPlaceholderText(_translate("CreateProduct", "precio"))
        self.input_category.setPlaceholderText(_translate("CreateProduct", "categoría"))
        self.btn_create.setText(_translate("CreateProduct", "AGREGAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateProduct = QtWidgets.QWidget()
    ui = Ui_CreateProduct()
    ui.setupUi(CreateProduct)
    CreateProduct.show()
    sys.exit(app.exec_())
