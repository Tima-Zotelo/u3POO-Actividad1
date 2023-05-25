import os
from Menu import Menu
from manejaFacultades import manejador

if __name__ == '__main__':
    manejador = manejador()
    bandera = False
    os.system('cls')
    menu = Menu()
    manejador.carga()
    while not bandera:
        menu.mostrar()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, manejador)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')