
'''
Created on Jan 19, 2015

@author: johanna
'''

import datetime


class TiempoMinimo(Exception):
    
    def __init__(self):
        self.msg = "Tiempo por debajo del minimo"

class TiempoMaximo(Exception):
    
    def __init__(self):
        self.msg = "Tiempo por encima del maximo"

class FechasErroneas(Exception):
    
    def __init__(self):
        self.msg = "Las fechas no concuerdan"
        
        
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
            try:
                print("Error en las fechas suministradas")
                raise FechasErroneas()
            except FechasErroneas:
                raise
        
        if tiempototal > datetime.timedelta(3):
            try:
                print("Excedidio el tiempo maximo")
                raise TiempoMaximo()
            except TiempoMaximo:
                raise
 

        elif tiempototal < datetime.timedelta(0,15*60,0):
            try:
                print("No cumple el tiempo minimo")
                raise TiempoMinimo()
            except TiempoMinimo:
                raise
        
        fraccion_hora = tiempototal.seconds%3600
        fraccion_hora = int(fraccion_hora/60)
        horas_aparcado = tiempototal.seconds//3600
        if fraccion_hora == 0 : horas_aparcado += 1
        horas_aparcado += (tiempototal.days*24)
        

        for i in range(0,horas_aparcado):
            
            if (f_en_comp + datetime.timedelta(hours=1)).hour == 6 :
                f_en_comp += datetime.timedelta(hours=1)
                totalPagar += int(self.tarif_Mayor())
            elif (f_en_comp + datetime.timedelta(hours=1)).hour == 18 :
                f_en_comp += datetime.timedelta(hours=1)
                totalPagar += int(self.tarif_Mayor())
            else :
                f_en_comp += datetime.timedelta(hours=1)
                if f_en_comp.hour in range(7,18):
                    totalPagar += int(self.tarif_d) 
                elif f_en_comp.hour in range(0,6) :
                    totalPagar += int(self.tarif_n)  
                elif f_en_comp.hour in range(19,24) :
                    totalPagar += int(self.tarif_n)                             

            
            
        if fraccion_hora != 0 :
            if f_en_comp.hour != (f_en_comp + datetime.timedelta(seconds = fraccion_hora*60) ).hour :
                f_en_comp += datetime.timedelta(seconds = fraccion_hora*60)
                if (f_en_comp.hour == 18 ) and f_en_comp.minute != 0 :
                    totalPagar += int(self.tarif_Mayor())
                elif (f_en_comp.hour == 6 ) and f_en_comp.minute == 0 :
                    totalPagar += int(self.tarif_Mayor())
                elif f_en_comp.hour in range(6,19):
                    totalPagar += int(self.tarif_d )
                elif f_en_comp.hour in range(18,24) :
                    totalPagar += int(self.tarif_n )
                elif f_en_comp.hour in range(0,6) :
                    totalPagar += int(self.tarif_n)
            else :
                if f_en_comp.hour in range(6,18):
                    totalPagar += int(self.tarif_d )
                elif f_en_comp.hour in range(18,24) :
                    totalPagar += int(self.tarif_n)
                elif f_en_comp.hour in range(0,6) :
                    totalPagar += int(self.tarif_n)
                    
        return totalPagar


if __name__ == "__main__":
    
    t_d = input("Introduce la tarifa diurna ");    
       
    t_n = input("Introduce la tarifa nocturna ");
    
    h_en = input("Introduce la hora de entrada HH:MM ");
    HE,ME = [int(a) for a in h_en.split(":")]
    
    h_sal = input("Introduce la hora de salida HH:MM ");
    HS,MS = [int(b) for b in h_sal.split(":")]
    
    f_en = input("Introduce la fecha entrada en el formato YYYY-MM-DD");
    YYYYE,MME,DDE = [int(c) for c in f_en.split("-")]
    
    f_sal = input("Introduce la fecha salida en el formato YYYY-MM-DD ");
    YYYYS,MMS,DDS = [int(d) for d in f_en.split("-")]
    
    tarif = Tarifa();
    tarif.tarif_d = t_d       
    tarif.tarif_n = t_n
    totalPagar = tarif.calcularTotal(YYYYE,MME,DDE,HE,ME,YYYYS,MMS,DDS,HS,MS)
    print("El total a pagar es: "+ str(totalPagar) + ("Bs"))