#Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.

precio=float(input("Ingresa el total de la cuenta "))

propina=input("De cuando desea incluir la propina: ")

if propina=="0":
    print (f"No hay propina, el total seria {precio}")
elif propina=="10":
    total1=(precio*0.10)+precio
    print(f"EL total de la comida incluyendo una propina del 10% es de:  ${total1}")
elif propina=="15":
    total2=(precio*0.15)+precio
    print(f"EL total de la comida incluyendo una propina del 15% es de: ${total2}")

elif propina=="20":
    total3=(precio*0.20)+precio
    print(f"El total de la comida incluyendo una propina del 20% es de : $,{total3}")
else:
    print("No hay propina")
