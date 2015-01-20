'''
Created on Jan 19, 2015

@author: johanna
'''

import datetime

class Tarifa:
    tarif_d = 0;
    tarif_n = 0;

    def calcularTotal(self, YYYYE,MME,DDE,HE,ME,YYYYS,MMS,DDS,HS,MS):
        
        h_en = datetime.time(HE,ME)
        h_sal = datetime.time(HS,MS)
        f_en = datetime.date(YYYYE,MME,DDE)
        f_sal =datetime.date(YYYYS,MMS,DDS)
        
        f_en_comp = datetime.datetime.combine(f_en, h_en)
        f_sal_comp = datetime.datetime.combine(f_sal, h_sal)
        if f_sal_comp > f_en_comp:
            f_completa_total = f_sal_comp - f_en_comp 
        elif f_sal_comp < f_en_comp:
            print("Fechas invalidas")
        else:
            print("Fechas invalidas")
        
        tiempototal = f_en_comp - f_sal_comp
        
        return tiempototal
        
''' M A I N '''
    
t_d = input("Introduce la tarifa diurna")    
   
t_n = input("Introduce la tarifa nocturna")

h_en = input("Introduce la hora de entrada HH:MM")
HE,ME = [int(a) for a in h_en.split(":")]

h_sal = input("Introduce la hora de salida HH:MM")
HS,MS = [int(b) for b in h_en.split(":")]

f_en = input("Introduce la fechaentrada YYYY-MM-DD")
YYYYE,MME,DDE = [int(c) for c in f_en.split("-")]

f_sal = input("Introduce la fechasalida YYYY-MM-DD")
YYYYS,MMS,DDS = [int(d) for d in f_en.split("-")]

tarif = Tarifa();
tarif.tarif_d = t_d
tarif.tarif_n = t_n
totalPagar = tarif.calcularTotal(YYYYE,MME,DDE,HE,ME,YYYYS,MMS,DDS,HS,MS)
print("El total a pagar es: "+ str(totalPagar))