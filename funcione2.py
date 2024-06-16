import os,csv,time,re
contactos = []
def opcion_1():
    os.system("cls")
    print(" \tAGREGAR UN CONTACTO ")
    print("Ingrese un nombre")
    while True:
        nombre = input("")
        if len(nombre)>3 and nombre.isalpha():
            break
        else:
            print("el nombre debe tener almenos 3 letras")
    print("Ingrese un número(celular)")
    while True:
        try:
            num=int(input(""))
            if num > 100000000 and num<999999999:
                break
            else:
                print("el número debe tener 9 díjitos")
        except:
            print("error, no debe llevar letras")

    print("Ingrese un correo")
    correo=input("")

    print("contacto agregado con éxito")
    contacto={
        "nombre":nombre,
        "numero":num,
        "correo":correo
    }
    contactos.append(contacto)



def opcion_2():
    os.system("cls")
    if len(contactos)==0:
        print("ningún contacto agregado")
    else:
        for lulo in contactos:
            print(f"nombre: {lulo["nombre"]}\nnúmero: {lulo["numero"]}\ncorreo: {lulo["correo"]}")



def opcion_3():
    if len(contactos)==0:
            print("ningún contacto agregado")
    else:
        conta = input("ingrese nombre del contacto(csv): ")
        with open(f"{conta}"+".csv", "w", newline="") as file:
            escritor=csv.writer(file)
            for x in contactos:
                for clave, valor in x.items():
                    escritor.writerow([clave])
                    escritor.writerow([valor])
                escritor.writerow("\n")
        print("el archivo csv se a creado")

def validar_correo(correo):
    return re.search(r"@.",correo) is not None

#retroalimentacion de como validar correo pls