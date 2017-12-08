from selenium import webdriver
from PageObjectLogin import LoginPage
from PageObjectCrearProducto import HomePage
from PageObjectCrearProducto import PaginaProductos
from PageObjectCrearProducto import CreacionProductos
from PageObjectEditarProducto import EditarProductosDeLaLista
import unittest
import time

class EditarP(unittest.TestCase):
        
        
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
        PaginaP.EntrarEditar()
                
                
    def test_EditarProductosDeLaLista(self):
        PaginaE = EditarProductosDeLaLista(self.driver)
        PaginaE.BotonEditProducto()
        PaginaE.Text_Nombre.clear()
        PaginaE.Text_Nombre = "Choripan"
        PaginaE.Text_Precio.clear()
        PaginaE.Text_Precio = "25.90"
        PaginaE.BotonGuardarCambios()
        PaginaE.EditadoExitoso()
                
                
    def tearDown(self):
        self.driver.quit()
                
if __name__ == '__main__':
    unittest.main()
