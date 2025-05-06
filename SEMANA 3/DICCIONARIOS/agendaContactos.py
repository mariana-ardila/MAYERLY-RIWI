agenda={ 
   "Juan": 3006041234,
   "Carlos":3104229850,
   "Mayerly": 3220544810,
   "Samuel": 3006045993,

}

def agregarContacto():
    nombre=input("Por favor ingrese el nombre del contacto: ")
    telefono=int(input("Por favor ingrese el telefono del contacto: "))
    agenda["nombre"]["nombre4"]=nombre
    agenda["telefono"]["telefono4"]=telefono
    print("Contacto agregado con exito")

def eliminarContacto(): 
    nombre=input("Por favor ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda["nombre"].values():
        index=list(agenda["nombre"].values()).index(nombre)
        agenda["nombre"].pop(f"nombre{index+1}")
        agenda["telefono"].pop(f"telefono{index+1}")
        print("Contacto eliminado con exito")
    else:
        print("Contacto no encontrado")

def bucarContacto():
    nombre=input("Por favor ingrese el nombre del contacto a buscar: ")
    if nombre in agenda["nombre"].values():
        index=list(agenda["nombre"].values()).index(nombre)
        print(f"Nombre: {agenda['nombre'][f'nombre{index+1}']}, Telefono: {agenda['telefono'][f'telefono{index+1}']}")
    else:
        print("Contacto no encontrado")

def listarContactos():
    if not agenda["nombre"]:
        print("No hay contactos registrados")
    else: 
        for i in range(len(agenda["nombre"])):
            print(f"Nombre: {agenda['nombre'][f'nombre{i+1}']}, Telefono: {agenda['telefono'][f'telefono{i+1}']}")
        print("Contactos listados con exito")
    print("Gracias por visitarnos")


while True:
    print ("BIENVENIDO A LA AGENDA DE MAYE")
    print ("1. Agregar contacto")
