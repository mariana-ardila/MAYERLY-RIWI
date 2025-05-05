
##VALOR MULTIPLES

def saludar(nombre, edad, apellido):

    print(f"Hola {nombre} {apellido}, tienes {edad} años")
saludar("MAYERLY", 20, "ZAPATA")

##VALOR POR DEFECTO INGRESADO POR EL USUARIO
##Cuando se define un valor por defecto, no es necesario ingresarlo al momento de llamar la funcion, se deja la funcioon vacia
def sumar(): ##definicion de la funcion
    a=int(input("ingrese el primer numero: ")) ##entrada de datos
    b=int(input("ingrese el segundo numero: "))
    c=int(input("ingrese el tercer numero: "))
    print("Los numeros son: ", a, b, c)
    print("La suma es: ", a+b+c)
sumar()
   


