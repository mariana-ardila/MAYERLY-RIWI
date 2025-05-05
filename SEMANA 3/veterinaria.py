##Desarrolla un programa en Python que permita gestionar información sobre animales. El programa debe tener un menú usando funciones con las siguientes opciones: 
#  recuerda que pasa nombre, edad y enfermo cada uno debe de guardarse en su propia lista


print ("BIENVENIDO A LA VETERINARIA MASCOTAS FELICES")
print ("1. Agregar mascota")
print ("2. Eliminar mascotas")
print ("3. Listar mascotas")
print ("4. Salir")

nombre=[]
edad=[]
enfermo=[]
match True:
    case True:
        opcion=int(input("Por favor ingrese la opcion deseada: "))
        if opcion==1:
          def agregarMascota():
            name=input("Por favor ingrese el nombre de la mascota: ")
            edad=int(input("Por favor ingrese la edad de la mascota: "))
            enfermo=input("La mascota esta enferma? (si/no): ").lower()
            if enfermo =="si":
                enfermo=True
            else:
                enfermo=False
            nombre.append(nombre)
            edad.append(edad)
            enfermo.append(enfermo)
            print("Mascota agregada con exito")
        elif opcion==2:
            def eliminarMascota():
                name=input("Por favor ingrese el nombre de la mascota a eliminar: ")
                if nombre in nombre:
                    index=nombre.index(nombre)
                    del nombre[index]
                    del edad[index]
                    del enfermo[index]
                    print("Mascota eliminada con exito")
                else:
                    print("La mascota no existe")
        elif opcion==3:
           def listarMascotas():
            for i in range(len(nombre)):
                print(f"Nombre: {nombre[i]}, Edad: {edad[i]}, Enfermo: {enfermo[i]}")
            print("Mascotas listadas con exito")
        elif opcion==4:
            print("Gracias por visitarnos")
    case False:
        print("Opcion no valida")
        print("Por favor ingrese una opcion valida")

while True:

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
        

            


    
