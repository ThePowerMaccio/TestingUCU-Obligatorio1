from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(PageObject):

	Productos = PageElement(id_ = "tab-products")

	def Entrar(self):
		self.Productos.click()
	
class PaginaProductos(PageObject):
	
	CrearProductos = PageElement(xpath = '//*[@id="content"]/div[1]/div[2]/div/a')
	BotonEditarProducto = PageElement(css = "#sub-nav > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
        BotonEditarPrimeroEnLista = PageElement(xpath = '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[2]/form/table/tbody/tr[2]/td[1]/a[1]')

	def Entrar(self):
		self.CrearProductos.click()

        def EntrarEditar(self):
                self.BotonEditarProducto.click()		
	
class CreacionProductos(PageObject):
	
	Nombre = PageElement(name = "name")
	Precio = PageElement(name = "price")
	Agregar = PageElement(name = "submit")
	Mensaje = PageElement (xpath = '//*[@id="create-edit-product"]/form/div[1]/div/span')
	
	
		
		
	def ElementoNoPresente(self, identificador):
                try:
                        WebDriverWait(self.w, 15).until(EC.visibility_of_element_located((By.XPATH, identificador)))
                        return True
		except TimeoutException:
                        return False	

        def AgregadoExitoso(self):
                assert self.Mensaje.text == "Update successful"

        def SinPrecio(self):
                assert self.ElementoNoPresente('//*[@id="create-edit-product"]/form/div[2]/div[1]/div/div[5]/span')

        def SinNombre(self):
                assert self.ElementoNoPresente('//*[@id="create-edit-product"]/form/div[2]/div[1]/div/div[1]/span')


        def Entrar(self):
		self.Agregar.click()



"""
//*[@id="create-edit-product"]/form/div[1]/div/span
Update successful
			
//*[@id="create-edit-product"]/form/div[2]/div[1]/div/div[5]/span
Missing Price
		
//*[@id="create-edit-product"]/form/div[2]/div[1]/div/div[1]/span
Missing Product Name"""
		
