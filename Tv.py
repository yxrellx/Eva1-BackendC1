from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self,Voltaje:int,precio:float,eficiencia:str,marca:str,tamano:str):
      super().__init__(Voltaje,precio,eficiencia,marca)
      self.__tamano = tamano
      
    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self,tamano):
        self.__tamano = tamano
        
    def imprimir_caracteristicas(self):
        return f'{super().imprimir_caracteristicas()} \n Tamaño: {self.__tamano} \n {self.calcularDescuento()}'