'''
Created on 20/1/2015

@author: Tony
'''

import unittest
from funcion.tarifa import Tarifa
from funcion.tarifa import TiempoMaximo
from funcion.tarifa import TiempoMinimo
from funcion.tarifa import FechasErroneas

class TestTarifa(unittest.TestCase):


    def testDiurno(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 5
        tarifatest.tarif_n = 2
        result = tarifatest.calcularTotal(1993,4,26,12,40,1993,4,26,13,0)
        self.assertEqual(result, 5,"Error al calcular el costo de estadia diurna")
        
    def testNocturno(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 5
        tarifatest.tarif_n = 2
        result = tarifatest.calcularTotal(1993,4,26,21,40,1993,4,26,23,45)
        self.assertEqual(result, 6,"Error al calcular el costo de estadia nocturna")

    def testCambioDiurNoc(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 5
        tarifatest.tarif_n = 2
        result = tarifatest.calcularTotal(1993,4,26,15,40,1993,4,26,20,45)
        self.assertEqual(result, 21,"Error al calcular el costo durante el cambio de tarifa")
        
    def testCambioNocDiur(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 5
        tarifatest.tarif_n = 2
        result = tarifatest.calcularTotal(1993,4,26,1,27,1993,4,26,10,30)
        self.assertEqual(result, 38,"Error al calcular el costo durante el cambio de tarifa")
        
    def testMinEstadia(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 5
        tarifatest.tarif_n = 2
        result = tarifatest.calcularTotal(1993,4,26,15,40,1993,4,26,15,55)
        self.assertEqual(result, 5,"Error al aplicar la estadia minima")
    
    def testMaxEstadia(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 1
        tarifatest.tarif_n = 2
        result = tarifatest.calcularTotal(1993,4,26,15,40,1993,4,29,15,40)
        self.assertEqual(result, 112,"Error al aplicar la estadia maxima")
        
    def testErrorFechas(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 1
        tarifatest.tarif_n = 2
        self.assertRaises(ValueError,tarifatest.calcularTotal,1993,4,95,6,0,1993,4,26,65,0)
        
    def testExcederTiempo(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 1
        tarifatest.tarif_n = 2
        self.assertRaises(TiempoMaximo,tarifatest.calcularTotal,1993,4,15,6,0,1993,4,30,5,0)
        
    def testTiempoInsuficiente(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 1
        tarifatest.tarif_n = 2
        self.assertRaises(TiempoMinimo,tarifatest.calcularTotal,1993,4,15,6,0,1993,4,15,6,10)
        
    def testFechasIncompatibles(self):
        tarifatest = Tarifa()
        tarifatest.tarif_d = 1
        tarifatest.tarif_n = 2
        self.assertRaises(FechasErroneas,tarifatest.calcularTotal,1993,4,15,6,0,1993,4,13,6,10)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()