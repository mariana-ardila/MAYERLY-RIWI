##PEDIR DOS VALORES AL USUARIO E IMPRIMIR LOS VALORES INTERCAMBIADOS

a=int(input("Por favor ingresa un numero:   "))
b=int(input("Por favor ingresa un numero;   "))

print(f"Los numeros que ingresaste fueron:  {a} , {b}")
      
a, b= b, a
print("Lus numeros intercambiados son: ", a, "y " ,b)
