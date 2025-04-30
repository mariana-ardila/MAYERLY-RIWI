#MIENTRAS I SEA MENOR A 6 SE VA A REPETIR

#WHILE CON ELSE

contraseñaC = "hola"
intentos = 3

while intentos > 0:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == contraseñaC:
        print("Bienvenido")
        break
    else:
        intentos = intentos -1
        print(f"Contraseña incorrecta. Te quedan {intentos} intento(s).")

if intentos == 0:
    print("Has agotado tus intentos. Acceso denegado.")
