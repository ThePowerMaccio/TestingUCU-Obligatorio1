from selenium import webdriver
from PageObjectLogin import LoginPage
import unittest
import time

class Logearse(unittest.TestCase):
        
        def setUp(self):
                self.driver = webdriver.Chrome() 
                self.driver.get("https://sandbox.2checkout.com/sandbox")
                
        def test_Entrar(self):
                PaginaL = LoginPage(self.driver)
                PaginaL.usuario = "UcuTesting2017"
                PaginaL.password = "Ucutest17"
                PaginaL.Entrar()
                assert PaginaL.ElementoNoPresente() == False
                #PaginaL.InicioFallido()

        def test_EntrarFallidoU(self):
                PaginaL = LoginPage(self.driver)
                PaginaL.usuario = "UcuTesting"
                PaginaL.password = "Ucutest17"
                PaginaL.Entrar()
                PaginaL.InicioFallido()

        def test_EntradaFallidaP(self):
                PaginaL = LoginPage(self.driver)
                PaginaL.usuario = "UcuTesting2017"
                PaginaL.password = "Ucutest"
                PaginaL.Entrar()
                PaginaL.InicioFallido()
                
                
        def tearDown(self):
                self.driver.quit()
                
if __name__ == '__main__':
    unittest.main()
