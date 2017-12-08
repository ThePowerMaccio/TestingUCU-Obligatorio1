from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class EliminarP(PageObject):

    botonEliminar = PageElement(xpath = '//*[@id="update_bulk"]/table/tbody/tr[3]/td/input')
    casilla = PageElement(name = "product_id")
    confirmar = PageElement(name="submit")
    status = PageElement(xpath = '//*[@id="content"]/div/div/div[1]/table/tbody/tr[2]/td[1]')

    def seleccionarE(self):
        self.casilla.click()

    def eliminarElemento(self):
        self.botonEliminar.click()

    def confirmarE(self):
        self.confirmar.click()

    def EliminacionExitosa(self):
        assert self.status.text == "Deleted"
