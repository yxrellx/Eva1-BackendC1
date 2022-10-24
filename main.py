from Consola import Consola
from Scooter import Scooter
from Bicicleta import Bicicleta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
from Tv import Tv

listaTvs = []
listaConsolas = []
listaScooters = []
listaBicicletas = []

def RegistrarTv():
    voltaje = int(input("Ingrese voltaje de la tv: "))
    precio = float(input("Ingrese precio de la tv: "))
    eficiencia = str(input("Ingrese eficiencia de la tv (A hasta F): ")).upper()
    marca = str(input("Ingrese marca de la tv: "))
    tamano = float(input("Ingrese tamano: "))
    tele = Tv(voltaje,precio,eficiencia,marca,tamano)
    listaTvs.extend([voltaje,precio,eficiencia,marca,tamano])
    #tele.imprimir_caracteristicas()

def Mostrar():
    print(listaTvs)
    print(listaConsolas)
    print(listaScooters)
    print(listaBicicletas)
    
def RegistrarConsola():
    voltaje = int(input("Ingrese voltaje de la consola: "))
    precio = float(input("Ingrese precio de la consola: "))
    eficiencia = str(input("Ingrese eficiencia de la consola (A hasta F): ")).upper()
    marca = str(input("Ingrese marca de la consola: "))
    version = str(input("Ingrese version de la consola: "))
    nombreConsola = str(input("Ingrese nombre de la consola: "))
    consola = Consola(voltaje,precio,eficiencia,marca,version,nombreConsola)
    listaConsolas.extend([voltaje,precio,eficiencia,marca,version,nombreConsola])
    #consola.imprimir_caracteristicas()

def RegistrarScooter():
    voltaje = int(input("Ingrese voltaje del scooters : "))
    precio = float(input("Ingrese precio del scooters: "))
    eficiencia = str(input("Ingrese eficiencia del scooters (A hasta F): ")).upper()
    marca = str(input("Ingrese marca del scooters: "))
    aro= float(input("Ingrese el aro del scooters: "))
    velocidad = int(input("Ingrese la velocidad del scooters: "))
    peso = float(input("Ingrese el peso del scooters: "))
    scooter = Scooter(voltaje,precio,eficiencia,marca,aro,velocidad,peso)
    listaScooters.extend([voltaje,precio,eficiencia,marca,aro,velocidad,peso])
    #scooter.imprimir_caracteristicas()

def RegistrarBicicleta():
    aro = float(input("Ingrese aro de la bicicleta: "))
    peso= float(input("Ingrese el peso de la bicicleta: "))
    precio = float(input("Ingrese el precio de la bicicleta: "))
    marca = str(input("Ingrese la marca de la bicicleta: "))
    bici= Bicicleta(aro,peso,precio,marca)
    listaBicicletas.extend([aro,peso,precio,marca])

def CotizarTvs():
    i= 0
    for t in listaConsolas:
        print(f'------ Consola {i + 1}-------')
        t.calcularDescuento()
        t.imprimir_caracteristicas()
        


def CotizarConsolas():
    i= 0
    for c in listaConsolas:
        print(f'------ Consola {i + 1}-------')
        c.calcularDescuento()
        c.imprimir_caracteristicas()

def CotizarScooters():
    i = 0
    for s in listaTvs:
        print(f'------ Scooters {i + 1}-------')
        s.calcularDespacho()
        s.imprimir_caracteristicas()

def CotizarBicicletas():
    i = 0
    for b in listaTvs:
        print(f'------ Bicicletas {i + 1}-------')
        b.calcularDespacho()
        b.imprimir_caracteristicas()























while True:
    print("------- Menu --------")
    print('1.- RegistrarTV')
    print('2.- RegistrarConsola')
    print('3.- Registrar Scooter')
    print('4.- RegistrarBicicleta')
    print('5.-Mostrar')
    print('6.-CotizarTvs')
    print('7.-CotizarConsolas')
    print('8.-CotizarScooters')
    print('9.-CotizarBicicletas')
    opcion = input("Ingrese una opcion: ")
    if opcion=='1':
        RegistrarTv()
    elif opcion=='2':
        RegistrarConsola()
    elif opcion=='3':
        RegistrarScooter()
    elif opcion=='4':
        RegistrarBicicleta()
    elif opcion=='5':
        Mostrar()
    elif opcion=='6':
        CotizarTvs()
    elif opcion=='7':
        CotizarConsolas()
    elif opcion=='8':
       CotizarScooters()
    elif opcion=='9':
       CotizarBicicletas()  

    else:
        print("Opcion invalida intente otra vez")