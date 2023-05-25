from carrera import Carrera

class Facultad:
    __codigo: int
    __nombre: str
    __direc: str
    __loc: str
    __tel: int
    __carrera = None

    def __init__(self, cod, nom, direc, loc, tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direc = direc
        self.__loc = loc
        self.__tel = tel
        self.__carrera = []

    def agregarC (self, xCod, xNom, xIni, xDur, xTit):
        xC = Carrera (xCod, xNom, xIni, xDur, xTit)
        self.__carrera.append (xC)

    def buscarC (self, xNom):
        i = 0
        ban = False
        while len (self.__carrera) -1 >= i and not ban:
            if self.__carrera[i].getNombre() != xNom:
                print ('No encontrao')
                i += 1
            else: 
                ban = True
                print ('siuuuuuu')
                return self.__carrera[i].getCodigo()
    
    def getCodigo(self):
        return self.__codigo
    
    def getNombre (self):
        return self.__nombre
    
    def getDireccion (self):
        return self.__direc
    
    def getLoc (self):
        return self.__loc
    
    def getTelefono(self):
        return self.__tel
    
    def getCarreras(self):
        return self.__carrera