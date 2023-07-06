
def llenadoAsientos(arreglo):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            if len(str(x))<2:
                arreglo[f][c]='0'+str(x)
            else:
                arreglo[f][c]=str(x)

def Compra(arreglo,numAsiento):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            if str(x)==numAsiento:
                print("XXX")