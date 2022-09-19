import sys
import os
#myDir = os.getcwd()
myDir = "C:/Users/Usuario/Desktop/CRUD_python_mysql"
sys.path.append(myDir)


from Database.Connexion import connection
from Models.Product import Product


class CreateProductController():

    def __init__(self,create_product):
        self.product = Product(connection())
        self.create_product = create_product


    def createProduct(self,cod,name,price,category,CreateProduct):
        if cod and name and price and category:
            self.product.insertProduct(cod,name,price,category)
            CreateProduct.hide()
