import sys
import os
#myDir = os.getcwd()
myDir = "C:/Users/Usuario/Desktop/CRUD_python_mysql"
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connexion import connection
from Models.User import User

class LoginController():
    def __init__(self, Log_in):
        self.user=User(connection())
        self.log_in=Log_in

    def logIn(self, user, password, Ui_Principal, LogIn):
        if user and password:
            user=self.user.getUser(user,password)
            if user:
                LogIn.hide()
                self.log_in.Form=QtWidgets.QMainWindow()
                self.log_in.ui=Ui_Principal()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                print("Logeado correctamente")
            else:
                print("ERROR")
