from page_objects import PageObject, PageElement
from selenium import webdriver


class EditarProductosDeLaLista(PageObject):
        Boton_Products = PageElement(id_= "tab-products")
        EditProducto = PageElement (xpath = '//*[@id="update_bulk"]/table/tbody/tr[2]/td[1]/a[1]')
        Text_Nombre = PageElement(name = "name")
        Text_Precio = PageElement(name = "price")
        GuardarCambios = PageElement(name = "submit")
        Mensaje = PageElement (xpath = '//*[@id="create-edit-product"]/form/div[1]/div/span')

        def BotonEditProducto(self):
                self.EditProducto.click()

        def BotonGuardarCambios(self):
                        self.GuardarCambios.click()

        def EditadoExitoso(self):
                assert self.Mensaje.text == "Update successful"
        
                
