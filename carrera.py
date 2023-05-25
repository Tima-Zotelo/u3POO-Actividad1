class Carrera:
    __cod: int
    __nom: str
    __inicio: str
    __dur: str
    __tit: str

    def __init__(self, cod, nom, ini, dur, tit) -> None:
        self.__cod = cod
        self.__nom = nom
        self.__inicio = ini
        self.__dur = dur
        self.__tit = tit

    def mostrarDatos (self, codF):
        codigo = (codF + 1) + self.__cod
        print(f'''
Codigo: {codigo}
Nombre: {self.__nom}
fecha de inicio: {self.__inicio}
Duracion: {self.__dur}
Titulo: {self.__tit}
''')

    def getCodigo (self):
        return self.__cod

    def getNombre (self):
        return self.__nom

    def getInicio (self):
        return self.__inicio

    def getDuracion (self):
        return self.__dur

    def getTitulo (self):
        return self.__tit