from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait



class LoginPage(PageObject):

	usuario = PageElement(name = "username")
	password = PageElement(id_= "password")
	login =PageElement(css = 'input[type="submit"]')
	#mensajeError =PageElement(id_ = "login-error" )
	
	def Entrar(self):
		self.login.submit()

	def ElementoNoPresente(self):
                try:
                        WebDriverWait(self.w, 15).until(EC.visibility_of_element_located((By.ID, "login-error")))
                        return True
		except TimeoutException:
                        return False	

        def InicioFallido(self):
                assert self.ElementoNoPresente() == True
