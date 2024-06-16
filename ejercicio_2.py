#ejercicio contacto
import time

from funcione2 import *

while True:
    print("""Lista de contactos
    1. agregar contacto
    2. mostrar contacto
    3. guardar contacto (csv)
    4. salir""")
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in(1,2,3,4):
                break
            else:
                print("opcion no valida")
        except():
            print("debe ser un numero porfavor")

    if opc == 1:
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc == 3:
        opcion_3()  
    elif opc == 4:
        print("sin bateria")
        break
    time.sleep(3)
