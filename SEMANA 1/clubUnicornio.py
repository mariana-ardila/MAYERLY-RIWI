edad=int(input("Por favor ingresa tu edad: "))


if edad>18:
    pase=input("¿Tienes pase?: ".lower())
    if edad>=18 and pase=="si":
        print("Tienes pase dorado, puedes entrar ")
    if edad>=18 and edad<=25 and pase=="no":
        print("Puedes entrar,cumples con la edad")
    if edad>25 and pase=="no":
        print("No puedes entrar, no tienes pase")
else:
    print("No puedes entrar, no cumples con las reglas")