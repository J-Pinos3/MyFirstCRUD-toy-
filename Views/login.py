import sys
import os
#myDir = os.getcwd()
myDir = "C:/Users/Usuario/Desktop/CRUD_python_mysql"
sys.path.append(myDir)

from Controllers.LoginController import LoginController
from Views.principal import Ui_Principal
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogIn(object):

    def __init__(self):
        self.login_controller=LoginController(self)


    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(764, 486)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 30, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.input_user = QtWidgets.QLineEdit(self.centralwidget)
        self.input_user.setGeometry(QtCore.QRect(280, 190, 241, 22))
        self.input_user.setObjectName("input_user")
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(280, 260, 241, 22))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(340, 330, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("background-color: rgb(28, 255, 187);\n"
"selection-color: rgb(28, 255, 187);\n"
"border-color: rgb(0, 0, 255);")
        self.btn_login.setObjectName("btn_login")
        LogIn.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LogIn)
        self.statusbar.setObjectName("statusbar")
        LogIn.setStatusBar(self.statusbar)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        #---------------------------------------EVENTS---------------------------------------
        self.x=self.btn_login.clicked.connect(lambda: self.login_controller.logIn(self.input_user.text(), self.input_password.text(), Ui_Principal, LogIn))

        #---------------------------------------END EVENTS---------------------------------------
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "MainWindow"))
        self.label.setText(_translate("LogIn", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">INICIAR SESIÓN</span></p></body></html>"))
        self.label_2.setText(_translate("LogIn", "Usuario:"))
        self.label_3.setText(_translate("LogIn", "Contraseña:"))
        self.input_user.setPlaceholderText(_translate("LogIn", "Usuario:"))
        self.input_password.setPlaceholderText(_translate("LogIn", "Contraseña:"))
        self.btn_login.setText(_translate("LogIn", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
