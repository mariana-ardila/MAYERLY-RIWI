agenda={ 
  "nombre":{
    
  },
  "telefono":{
   
  }
}

def agregarContacto():
    nombre=input("Por favor ingrese el nombre del contacto: ")
    telefono=int(input("Por favor ingrese el telefono del contacto: "))
    agenda["nombre"]["nombre"]=nombre
    agenda["telefono"]["telefono"]=telefono
    print("Contacto agregado con exito")

def eliminarContacto(): 
    nombre=input("Por favor ingrese el nombre del contacto a eliminar: ").lower()
    if nombre in agenda["nombre"].values():
        index=list(agenda["nombre"].values()).index(nombre)
        agenda["nombre"].pop(f"nombre{index+1}")
        agenda["telefono"].pop(f"telefono{index+1}")
        print("Contacto eliminado con exito")
    else:
        print("Contacto no encontrado")

def bucarContacto():
    nombre=input("Por favor ingrese el nombre del contacto a buscar: ").lower()
    if nombre in agenda["nombre"].values():
        index=list(agenda["nombre"].values()).index(nombre)
        print(f"Nombre: {agenda['nombre'][f'nombre{index+1}']}, Telefono: {agenda['telefono'][f'telefono{index+1}']}")
    else:
        print("Contacto no encontrado")

def listarContactos():
    if not agenda["nombre"]:
        print("No hay contactos registrados")
    else: 
        for i, nombre in enumerate(agenda["nombre"].values(), start=1):
            print(f"{i}. Nombre: {nombre}, Telefono: {agenda['telefono'].get(f'telefono{i}', 'No disponible')}")
        print("Contactos listados con exito")
    print("Gracias por visitarnos")


while True:
    print ("BIENVENIDO A LA AGENDA DE MAYE")
    print ("1. Agregar contacto")
    print ("2. Eliminar contacto")
    print ("3. Buscar contacto")
    print ("4. Listar contactos")
    print ("5. Salir")
    try: 
        opcion=int(input("Por favor ingrese una opcion: "))
    except ValueError:
        print("Opcion no valida, por favor ingrese un numero")
        continue
    if opcion==1:
        agregarContacto()
    elif opcion==2:      
        eliminarContacto()
    elif opcion==3: 
        bucarContacto()
    elif opcion==4:
        listarContactos()
    elif opcion==5:
        print("Gracias por visitarnos")
        break
    else:
        print("Opcion no valida")
               
