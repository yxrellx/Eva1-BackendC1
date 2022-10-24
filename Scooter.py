from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia,Transporte):
    def __init__(self,Voltaje:int,precio:float,eficiencia:str,marca:str,aro:float,velocidad:int,peso:float):
        super().__init__(Voltaje,precio,eficiencia,marca)
        Transporte.__init__(self)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        
    def get_aro(self):
        return self.__aro
    
    def get_velocidad(self):
        return self.__velocidad  
    
    def get_peso(self):
        return self.__peso 
    
    def set_aro(self,aro):
        self.__aro = aro
    
    def set_velocidad(self,velocidad):
        self.__velocidad = velocidad

    def set_peso(self,peso):
        self.__peso = peso
        
    def calcularDespacho(self):
        valor = self.__peso * 300
        despacho = super().calcularDespacho() + valor
        total = self.get_precio + despacho
        print(f'El total es: {total}')
        
    def imprimir_caracteristicas(self):
        return f'{super().imprimir_caracteristicas()} \n  Aro: {self.__aro}  \n Velocidad: {self.__velocidad}  \n  Peso:{self.__peso} \n Descuento: {self.calcularDescuento()} \n CostoDespacho: {self.calcularDespacho()} '