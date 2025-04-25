puntaje=0


pregunta=int(input("¿QUE EDAD TIENES?: "))
if pregunta>=22:
    puntaje=puntaje+20
    pregunta1=input("¿Eres aseado?:")
    if pregunta1=="si":
        puntaje=puntaje+30
        pregunta2=input("¿Te cepillas los dientes?: ")
        if pregunta2=="si":
            puntaje=puntaje+15
        elif pregunta2=="a veces":
                puntaje=puntaje+5


    pregunta3=input("¿Te  gustan los animales?: ")
    if pregunta3=="si":
        puntaje=puntaje+20
        pregunta4=input("¿Tienes mascotas?: ")
        if pregunta4=="si":
            puntaje=puntaje+15
        elif pregunta4=="no":
            puntaje=puntaje+5
    else:
        puntaje=puntaje+0

    pregunta5=input("¿Te gusta viajar?: ")
    if pregunta5=="si":
        puntaje=puntaje+15
    else:
        puntaje=puntaje+0

    pregunta6=input("¿Pasas tiempo de calidad con tu familia?: ")
    if pregunta6=="si":
        puntaje=puntaje+15
        pregunta7=input("¿Tienes hijos?: ")
        if pregunta7=="si":
            puntaje=puntaje-20
        else:
            puntaje=puntaje-20
        pregunta8=input("¿Quieres tener hijos?: ")
        if pregunta8=="si":
            puntaje=puntaje+0
    else:
            puntaje=puntaje-10

    pregunta9=input("¿Estas trabajando?: ")
    if pregunta9=="si":
        puntaje=puntaje+15
        pregunta10=input("¿Te gusta estudiar?: ")
        if pregunta10=="si":
            puntaje=puntaje+15
        pregunta11=input("¿Te gusta salir?: ")
        if pregunta11=="si":
            puntaje=puntaje+15
        else:
            puntaje=puntaje-5
    else:
        puntaje=puntaje-50
else: 
    print("No aplicas amiguito, estas muy niño")






print(f"El total de tu puntaje es de {puntaje}")

if puntaje>=100:
    print("Eres mi chico ideal")
elif puntaje>=50:
    print("Todavia te falta, trabaja un poquito mas")
else:
    print("No aplicas, lo siento")