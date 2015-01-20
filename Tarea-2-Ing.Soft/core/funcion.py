'''
Created on Jan 19, 2015

@author: johanna
'''

import datetime

class Tarifa:
    tarif_d = 0;
    tarif_n = 0;
    
    def tarif_Mayor(self):
        if self.tarif_d > self.tarif_n: return self.tarif_d
        else: return self.tarif_n

    def calcularTotal(self, YYYYE,MME,DDE,HE,ME,YYYYS,MMS,DDS,HS,MS):
        
        h_en = datetime.time(HE,ME)
        h_sal = datetime.time(HS,MS)
        f_en = datetime.date(YYYYE,MME,DDE)
        f_sal =datetime.date(YYYYS,MMS,DDS)
        totalPagar = 0
        
        f_en_comp = datetime.datetime.combine(f_en, h_en)
        f_sal_comp = datetime.datetime.combine(f_sal, h_sal)
        
        if f_sal_comp > f_en_comp:
            tiempototal = f_sal_comp - f_en_comp
        elif f_sal_comp <= f_en_comp:
            print("Fechas invalidas")
            return None
        
        if tiempototal > datetime.timedelta(3):
            print("Excedidio el tiempo maximo")
            return None
        elif tiempototal < datetime.timedelta(0,15*60,0):
            print("No cumple el tiempo minimo")
            return None
        
        fraccion_hora = tiempototal.seconds%3600
        fraccion_hora = int(fraccion_hora/60)
        horas_aparcado = tiempototal.seconds//3600
        #if fraccion_hora != 0 : horas_aparcado += 1
        horas_aparcado += (tiempototal.days*24)
        
        for i in range(1,horas_aparcado+1):
            if (f_en_comp + datetime.timedelta(hours=1)).hour == (6 or 18) :
                f_en_comp += datetime.timedelta(hours=1)
                totalPagar += self.tarif_Mayor()
            else :
                f_en_comp += datetime.timedelta(hours=1)
                if f_en_comp.hour in range(7,17):
                    totalPagar += self.tarif_d 
                elif f_en_comp.hour in range(19,24) or range(0,6) :
                    totalPagar += self.tarif_n                            
            print(totalPagar)
            print(f_en_comp)
            print("horas " + str(i))
        if fraccion_hora != 0 :
            if f_en_comp.hour != (f_en_comp + datetime.timedelta(seconds = fraccion_hora*60) ).hour :
                f_en_comp += datetime.timedelta(seconds = fraccion_hora*60)
                if (f_en_comp.hour == (18 or 6) ) :
                    totalPagar += self.tarif_Mayor()
                elif f_en_comp.hour in range(7,18):
                    totalPagar += self.tarif_d 
                elif f_en_comp.hour in range(19,24) or range(0,6) :
                    totalPagar += self.tarif_n 
            else :
                if f_en_comp.hour in range(6,17):
                    totalPagar += self.tarif_d 
                elif f_en_comp.hour in range(19,24) or range(0,6) :
                    totalPagar += self.tarif_n 
                    
        print(totalPagar)
        print(tiempototal)
        return totalPagar
        
''' M A I N '''
"""    
t_d = input("Introduce la tarifa diurna")    
   
t_n = input("Introduce la tarifa nocturna")

h_en = input("Introduce la hora de entrada HH:MM")
HE,ME = [int(a) for a in h_en.split(":")]

h_sal = input("Introduce la hora de salida HH:MM")
HS,MS = [int(b) for b in h_sal.split(":")]

f_en = input("Introduce la fechaentrada YYYY-MM-DD")
YYYYE,MME,DDE = [int(c) for c in f_en.split("-")]

f_sal = input("Introduce la fechasalida YYYY-MM-DD")
YYYYS,MMS,DDS = [int(d) for d in f_en.split("-")]
"""
tarif = Tarifa();
"""tarif.tarif_d = t_d       
tarif.tarif_n = t_n"""
tarif.tarif_d = 1
tarif.tarif_n = 5
"""totalPagar = tarif.calcularTotal(YYYYE,MME,DDE,HE,ME,YYYYS,MMS,DDS,HS,MS)"""
totalPagar = tarif.calcularTotal(1993,4,26,13,40,1993,4,26,18,0)
print("El total a pagar es: "+ str(totalPagar))


1440 = 1
1540 = 2
1640 = 3
1740 = 4
18 = 5