from selenium import webdriver
from PageObjectLogin import LoginPage
import unittest
import time
from PageObjectCrearProducto import HomePage
from PageObjectCrearProducto import PaginaProductos
from PageObjectCrearProducto import CreacionProductos

class IngresarP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://sandbox.2checkout.com/sandbox")
        
        PaginaL = LoginPage(self.driver)
        PaginaL.usuario = "UcuTesting2017"
        PaginaL.password = "Ucutest17"
        PaginaL.Entrar()

        PaginaH = HomePage(self.driver)
        PaginaH.Entrar()

        PaginaP = PaginaProductos(self.driver)
        PaginaP.Entrar()

        
    def test_CrearProductoCorrecto(self):

        PaginaCP = CreacionProductos(self.driver)
        PaginaCP.Nombre = "Nuevo prodcuto 1"
        PaginaCP.Precio = 200
        PaginaCP.Entrar()
        PaginaCP.AgregadoExitoso()

    def test_CrearProductoFaltaNombre(self):

        PaginaCP = CreacionProductos(self.driver)
        PaginaCP.Nombre = ""
        PaginaCP.Precio = 200
        PaginaCP.Entrar()
        PaginaCP.SinNombre()
        
    def test_CrearProductoFaltaPrecio(self):

        PaginaCP = CreacionProductos(self.driver)
        PaginaCP.Nombre = "Nuevo Producto 2"
        
        PaginaCP.Entrar()
        PaginaCP.SinPrecio()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
