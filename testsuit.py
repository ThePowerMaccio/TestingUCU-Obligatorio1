import unittest
from IngresoPagina import Logearse
from IngresarProductos import IngresarP
from EditarProductosDeLaLista import EditarP
from EliminarProducto import EliminarP
import HTMLTestRunner
import os




# obtengo path para localizar donde escribir el reporte
dir = os.getcwd()

# obtener los casos de test de SearchText
Logeos = unittest.TestLoader().loadTestsFromTestCase(Logearse)

IngresoProductos = unittest.TestLoader().loadTestsFromTestCase(IngresarP)

Edicion = unittest.TestLoader().loadTestsFromTestCase(EditarP)

Eliminacion = unittest.TestLoader().loadTestsFromTestCase(EliminarP)

# creamos un test suite
test_suite = unittest.TestSuite([Logeos, IngresoProductos, Eliminacion])

# creo archivo de reporte
outfile = open(dir + "\TestSummary.html", "w+")

# configuro opciones de HTMLTestRunner
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

# ejecutamos usando HTMLTestRunner
runner.run(test_suite)
