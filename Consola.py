from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self,Voltaje:int,precio:float,eficiencia:str,marca:str,nombre_consola:str,version:str):
        super().__init__(Voltaje,precio,eficiencia,marca)
        self.__nombre_consola = nombre_consola
        self.__version = version
        
    def get_nombre_consola(self):
        return self.__nombre_consola
        
    def get_version(self):
        return self.__version
    
    def set_nombre_consola(self,nombre_consola):
        self.__nombre_consola = nombre_consola
        
    def set_version(self,version):
        self.__version = version
        
    def calcularDescuento(self,Version):
        if Version=='Lite':
            descuento = self.__precio * 0.05
        else:
            descuento = 0
        
        v_total = super().calcularDescuento() + descuento
        print(f'Su total es: {v_total}')
   
    def imprimir_caracteristicas(self):
        return f'{super().imprimir_caracteristicas()} \n Nombre: {self.__nombre_consola} \n Versión: {self.__version}'
