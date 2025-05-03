# Entrada de calificaciones
inicio = input("Ingresa una lista de calificaciones separadas por comas (ej. 3.5, 4.0, 2.5): ")

calificaciones = []  # Creamos lista vacía para almacenar las calificaciones

# Convertir la cadena de entrada en una lista de números flotantes
for numero in inicio.split(","):
    calificaciones.append(float(numero.strip()))

# Mostrar la lista de calificaciones ya convertida
print("Lista de calificaciones:", calificaciones)

# Validar entrada hasta que se ingrese una calificación existente
while True:
    calificacion_buscada = float(input("Ingresa la calificación a buscar: "))
    if calificacion_buscada in calificaciones:
        break
    else:
        print("LA CALIFICACIÓN BUSCADA NO ESTÁ EN LA LISTA. INTENTA DE NUEVO.")

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

# Contar cuántas calificaciones son mayores al valor buscado
contador_may = 0
i = 0
while i < len(calificaciones):
    if calificaciones[i] > calificacion_buscada:
        contador_may += 1
    i += 1
print("La cantidad de calificaciones mayores a", calificacion_buscada, "es:", contador_may)

# Contar cuántas veces aparece la calificación buscada
contador_iguales = 0
for calificacion in calificaciones:
    if calificacion == calificacion_buscada:
        contador_iguales += 1
print("La calificación buscada aparece", contador_iguales, "veces en la lista")
