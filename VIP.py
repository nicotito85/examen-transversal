class VIP:


    nombreAsistente=''
    apellidoAsistente=''
    rutAsistente=1111111
    numAsiento=0


    def __init__(self):
        self.nombreAsistente='s/n'
        self.apellidoAsistente="s/n"
        self.rut=1111111
        self.numAsiento=1


    def setnombreAsistente(self, nombreAsistente):
        if len(nombreAsistente)>=2 and nombreAsistente.isalpha():
            self.nombreAsistente=nombreAsistente
            return False

    def setpellidoAsistente(self,apellidoAsistente):
        if len(apellidoAsistente)>=2 and apellidoAsistente.isaplha():
            self.apellidoAsistente=apellidoAsistente
            return False

    def setrutAsistente(self,rutAsistente):
        if rutAsistente>=10000000:
            self.rutAsistente=rutAsistente
            return False

