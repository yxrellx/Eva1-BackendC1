class Tecnologia:
    def __init__(self,Voltaje:int,precio:float,eficiencia:str,marca:str):
        self.__voltaje = Voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        if eficiencia == "A" or eficiencia=="B":
           self.__descuento = 0.5
        elif eficiencia == "C" or eficiencia=="D":
            self.__descuento = 0.3
        elif eficiencia == "E" or eficiencia=="F":
            self.__descuento =  0.1
        else:
          self.__descuento = 0  
        self.__marca = marca
        
    def get_voltaje(self):
        return self.__voltaje
    
    def get_precio(self):
        return self.__precio
    
    def get_eficiencia(self):
        return self.__eficiencia
    
    def get_marca(self):
        return self.__marca
    
    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje
        
    def set_precio(self,precio):
        self.__precio = precio
        
    def set_eficiencia(self,eficiencia):
        self.__eficiencia = eficiencia
        
    def set_marca(self,marca):
        self.__marca = marca
        
    
    def calcularDescuento(self):
        if self.__descuento ==0:
            print(f'No hay descuento. \n Total: {self.__precio}')
        else:
            resultado = self.__precio - (self.__descuento * self.__precio)
            print(f'El descuento por eficiencia es: {self.__eficiencia}: {self.__descuento} \n Total: {resultado}')
       
           
    def imprimir_caracteristicas(self):
        return f'Caracteristicas generales: /n Voltaje: {self.__voltaje} \n  Precio: {self.__precio} \n  Eficiencia: {self.__eficiencia} \n Marca: {self.__marca}'
        