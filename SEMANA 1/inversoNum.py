
num1=int(input("Ingrese un numero de tres cifras "))

if num1 >= 100 and num1 <= 999:

    centena = num1 // 100
    decena = (num1//10) % 10
    unidades = num1 % 10

print(centena,decena,unidades)
print(unidades,decena,centena)