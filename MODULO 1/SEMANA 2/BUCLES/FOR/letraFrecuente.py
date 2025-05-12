palabra=input("Por favor ingresa una palabra: ")
frecuencia={}

for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra]=frecuencia[letra]+1
    else:
        frecuencia[letra]=1

letraFrecuencia=''
frecuenciaMayor=0

for letra in frecuencia:
    if frecuencia[letra]>frecuenciaMayor:
        frecuenciaMayor=frecuencia[letra]
        letraFrecuencia=letra
print("La letra que mas se repite es: " , letraFrecuencia)
print("Y se repite ", frecuenciaMayor , "veces")
    

################
