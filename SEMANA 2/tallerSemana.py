# Entrada de calificaciones con validación
while True:
    inicio = input("Ingresa una lista de calificaciones separadas por comas (ej. 3.5, 4.0, 2.5): ")
    calificaciones = []
    entrada_valida = True 

### Validar que la entrada este en el formato correcto y que las calificaciones sean números entre 0.0 y 5.0
    for numero in inicio.split(","):
        try:
            calificacion = float(numero.strip())
            if 0.0 <= calificacion <= 5.0:
                calificaciones.append(calificacion)
            else:
                print(f"Error: La calificación {calificacion} está fuera del rango permitido (0.0 a 5.0).")
                entrada_valida = False
                break
        except ValueError:
            print(f"Error: '{numero}' no es un número válido.")
            entrada_valida = False
            break

    if entrada_valida:
        break 

# Mostrar la lista de calificaciones ya convertida
print("Lista de calificaciones:", calificaciones)

# Validar entrada hasta que se ingrese una calificación existente y válida
while True:
    try:
        calificacion_buscada = float(input("Ingresa la calificación a buscar (entre 0.0 y 5.0): "))
        if not (0.0 <= calificacion_buscada <= 5.0):
            print("Error: La calificación debe estar entre 0.0 y 5.0.")
        elif calificacion_buscada not in calificaciones:
           print("La calificación buscada no está en la lista. Intenta de nuevo.") 
        else:
            break
    except ValueError:
        print("Error: Debes ingresar un número válido.")

print("Calificación buscada:", calificacion_buscada)

# Recorre la lista y muestra si está aprobada o reprobada
for calificacion in calificaciones:
    if calificacion >= 3.0:
        print("La calificación", calificacion, "¡Materia aprobada!")
    else:
        print("La calificación", calificacion, "¡Materia reprobada!")

# Calcular el promedio
suma = 0
for calificacion in calificaciones:
    suma += calificacion
promedio = suma / len(calificaciones)
print("El promedio de las calificaciones es:", promedio)
if promedio >= 3.0:
    print("¡Curso aprobado!")
else:
    print("¡Curso reprobado!")

# Contar cuántas calificaciones son mayores al valor buscado
contador_may = 0
i = 0
while i < len(calificaciones):
    if calificaciones[i] > calificacion_buscada:
        contador_may += 1
    i += 1
print("La cantidad de calificaciones mayores a", calificacion_buscada, "es:", contador_may)

# Contar cuántas veces aparece la calificación buscada, usando break y continue
contador_iguales = 0
for calificacion in calificaciones:
    if calificacion != calificacion_buscada:
        continue
    contador_iguales += 1

print("La calificación buscada aparece", contador_iguales, "veces en la lista")

