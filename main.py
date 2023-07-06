#ce=compra entradas
from Funciones import *
from VIP import *
import numpy as np
arreglo=np.full([10, 10],"---")
listaVip=[]
cicle=True
p = 0
cp = 0
g = 0
cg = 0
s = 0
cs = 0


def Salida():
    print("Gracias por si atencion")
    print("Niolas Soto Zeballos 06/07/23")
    return False

def compraEntradas(arreglo,listaVip):

    v=VIP()
    z = False
    while z==False:
        v.setrutAsistente=int(input("ingrese su rut porfavor"))
        z=False

        v.setnombreAsistente=input("porfavor ingrese su nombre")
        z=False

        v.setpellidoAsistente=input("porfavor ingrese su apellido")


        ce=int(input("cuantas entradas desea comprar?1-3"))
        if ce>=1 and ce<=3:
            print("Entradas")
            print("----------------------------------------")
            print("entrada Silver=50.000---asientos del 51 al 100")
            print("entrada Gold=80.000---asientos del 21 al 50")
            print("entrada Platinum=120.000---asientos del 1 al 20")
            te=int(input("porfavor escoja su asiento para darle su entrada"))
            if te>=1 and te<=20:
                v.numAsiento=te


            if te>=21 and te<=50:
                v.numAsiento=te

            if te>=51 and te<=100:
                v.numAsiento=te


            else:
                print("porfavor escoja una opcion valida")

            listaVip.append(v)
            print("operacion realizada")
            break
        else:
            print("porfavor ingrese una cantidad de 1 a 3")

def MostrarVisitante(arreglo,listaVip):
    print("Listado Asitentes")
    for rutAsistente in listaVip:
        print(f"{rutAsistente}")


def MostrarTotales(arreglo,listaVip):
    print(f"cantidad entradas silver{cs} total:{s}")
    print(f"cantidad entradas gold{cg} total{g}")
    print(f"cantidad entradas platinum{cp}total{p}")



while cicle:
    print("productora eventos Creativos.cl")
    print("1)Comprar entradas")
    print("2)Mostrar ubicaciones disponibles")
    print("3)Ver listado asistentes")
    print("4)Mostrar ganancias Totales")
    print("5)Salir")
    try:
        op=int(input("porfavor escoja una opcion"))
        match op:
            case 1:
                compraEntradas(arreglo,listaVip)
            case 2:
                llenadoAsientos(arreglo)
                print(arreglo)
            case 3:
                MostrarVisitante(listaVip,arreglo)
            case 4:
                MostrarTotales(arreglo,listaVip)
            case 5:
                cicle = Salida()
            case _:
                print("opcion invalida porfavor intentelo de nuevo")

    except BaseException as error:
        print(f"error",{error})