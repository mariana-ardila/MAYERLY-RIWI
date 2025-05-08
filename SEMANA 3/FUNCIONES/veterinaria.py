##Desarrolla un programa en Python que permita gestionar información sobre animales. El programa debe tener un menú usando funciones con las siguientes opciones: 
#  recuerda que pasa nombre, edad y enfermo cada uno debe de guardarse en su propia lista


nombre=[]
edad=[]
enfermo=[]

def agregarMascota():
    name=input("Por favor ingrese el nombre de la mascota: ")
    eda=input("Por favor ingrese la edad de la mascota: ")
    enfer=input("La mascota esta enferma? (si/no): ").lower()
    if enfer =="si":
        enfer=True
    else:
        enfer=False
    nombre.append(name)
    edad.append(eda)
    enfermo.append(enfer)
    print("Mascota agregada con exito")
        

def eliminarMascota():
    name=input("Por favor ingrese el nombre de la mascota a eliminar: ")
    if name in nombre:
        index=nombre.index(name)
        nombre.pop(index)
        edad.pop(index)
        enfermo.pop(index)

    print("Mascota eliminada con exito")
    

def listarMascotas():
    if not nombre:
        print("No hay mascotas registradas")
    else: 
        for i in range(len(nombre)):
            estado="Enfermo" if enfermo[i] else "Sano"
            print(f"Nombre: {nombre[i]}, Edad: {edad[i]}, Estado: {estado}")
            print("Mascotas listadas con exito")
    print("Gracias por visitarnos")
    

while True:
    print ("BIENVENIDO A LA VETERINARIA MASCOTAS FELICES")
    print ("1. Agregar mascota")
    print ("2. Eliminar mascotas")
    print ("3. Listar mascotas")
    print ("4. Salir")

    try: 
        opcion=int(input("Por favor ingrese una opcion: "))
    except ValueError:
        print("Opcion no valida, por favor ingrese un numero")
        continue
    if opcion==1:
        agregarMascota()
    elif opcion==2:
        eliminarMascota()
    elif opcion==3:
        listarMascotas()
    elif opcion==4:
        print("Gracias por visitarnos")
        break
    else:
        print("Opcion no valida")
        




    

