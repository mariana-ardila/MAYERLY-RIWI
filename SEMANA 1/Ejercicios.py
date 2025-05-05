name1 =  str(input("por favor ingrese el primer nombre: "))
name2 =  str(input("por favor ingrese segundo nombre: "))
age1 = int(input("por favor ingrese la edad de la primera persona: "))
age2 = int(input("por favor ingrese la edad de la segunda persona: "))
if age1 > age2 :
    print(f"{name1} es mayor")
elif age2  > age1 :
    print(f"{name2} es mayor")
else : 
    print("ambos tienen la misma edad")

if age1 >=  18 :
    print(f"{name1} es mayor de edad")
else: print(f"{name1} es menor de edad")

if age2 >= 18 :
    print(f"{name2} es mayor de edad")
else: print(f"{name2} es menor de edad")
    