from selenium import webdriver
from PageObjectLogin import LoginPage
import unittest
import time
from PageObjectCrearProducto import HomePage
from PageObjectCrearProducto import PaginaProductos
from PageObjectCrearProducto import CreacionProductos
from PageObjectEliminar import EliminarP

class EliminarP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://sandbox.2checkout.com/sandbox")
        
        PaginaL = LoginPage(self.driver)
        PaginaL.usuario = "UcuTesting2017"
        PaginaL.password = "Ucutest17"
        PaginaL.Entrar()

        PaginaH = HomePage(self.driver)
        PaginaH.Entrar()

        
    def test_EliminarProducto(self):

        PaginaE = EliminarP(self.driver)
        PaginaE.seleccionarE()
        PaginaE.eliminarElemento()
        PaginaE.confirmarE()
        PaginaE.EliminacionExitosa()


    def tearDown(self):
        self.driver.quit()
                
if __name__ == '__main__':
    unittest.main()
