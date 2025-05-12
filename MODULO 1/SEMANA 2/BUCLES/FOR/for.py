nombre="MAYERLY ZAPATA"
for i in range (3):
    print(nombre)

for x in "Banana":
    print(x)

#SE ROMPE CUANDO LLEGA A LA POSICION BANANO
frutas=["uva", "pera", "banano", "mango"]
for x in "banano":
    print(x)
    if x =="banano":
        break

## imprime con saltos
for i in range(1,20,3):
    print(i)

#imprime un mensaje cuando el ciclo haya terminado
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("El proceso terminó")


  #BUCLES DESGASTADOS (ANIDADOS)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
     print(x,y) #me imprime cada adjetivo con cada fruta


nombre=["MAYERLY", "VALERIA", "VALENTINA"]
adjetivo=["ZAPATA", "RODRIGUEZ"]

for i in adjetivo:
    for a in nombre:
       print(a,i)