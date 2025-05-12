palabra = input("Por favor ingresa una palabra: ")

letras_contadas = []
letraFrecuencia = ''
frecuenciaMayor = 0

for letra in palabra:
    if letra not in letras_contadas:
        contador = 0
        for l in palabra:
            if l == letra:
                contador += 1
        letras_contadas.append(letra)
        if contador > frecuenciaMayor:
            frecuenciaMayor = contador
            letraFrecuencia = letra

print("La letra que más se repite es:", letraFrecuencia)
print("Y se repite", frecuenciaMayor, "veces")
