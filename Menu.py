import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            0: self.salir
                        }
        
    def opcion(self,op, manejador):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2:
            func(manejador)
        else:
            func()

    def mostrar (self):
        print("""
---------->Menu Principal<----------

-> 1: Mostrar carreras y duracion de una facultad
-> 2: Mostrar una carrera
-> 0: Salir del programa
""")

## OPCIONES
    def opc1 (self, manejador):
        os.system('cls')
        c = int (input ('ingrese codigo de facultad: '))
        manejador.mostrarF(c)

    def opc2 (self, manejador):
        os.system('cls')
        nom = input ('ingrese nombre de carrera: ')
        manejador.mostrarC(nom)

    def salir (self):
        print ('saliendo...')
