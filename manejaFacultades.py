import csv
from facultad import Facultad as fd

class manejador:
    __listaF: list
    def __init__(self) -> None:
        self.__listaF = []

    def agregarF (self, xF):
        self.__listaF.append(xF)

    def carga (self):
        path = './Facultades.csv'
        archivo = open (path, 'r')
        reader = csv.reader (archivo, delimiter=',')
        for fila in reader:
            if len (fila) == 5:
                cod = int (fila[0])
                nom = fila [1]
                direc = fila [2]
                loc = fila [3]
                tel = fila [4]
                xFacultad = fd (cod, nom, direc, loc, tel)
                self.agregarF (xFacultad)
            else:
                codF = int (fila [0])
                codC = int (fila [1])
                nom = fila [2]
                inicio = fila [3]
                dur = fila [4]
                tit = fila [5]
                self.__listaF[codF-1].agregarC (codC, nom, inicio, dur, tit)

    def mostrarF (self, c):
        for f in self.__listaF:
            if f.getCodigo() == c:
                print (f'''
Facultad: {f.getNombre()}
Carreras:''')
                for car in f.getCarreras():
                    print (f'''
Nombre: {car.getNombre()}
Duracion: {car.getDuracion()}
---------------------------------------------------''')

    def mostrarC (self, xnom):
        i = 0
        r = len (self.__listaF) - 1
        bandera = False
        while i <= r and not bandera:
            xc = int (self.__listaF[i].buscarC(xnom))
            if xc == None:
                i += 1
            else: bandera = True
        print (f'''
Carrera: {xnom}
codigo: {self.__listaF[i].getCodigo()} {xc}
Facultad: {self.__listaF[i].getNombre()}
Localidad: {self.__listaF[i].getLoc()}
''')

