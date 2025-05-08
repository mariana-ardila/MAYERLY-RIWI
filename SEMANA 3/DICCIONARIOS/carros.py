carros={
    "marca": "ford",
    "modelo": "mustang",
    "año": 2020,
    "color": "rojo",
    "kilometraje": 15000,
    "precio": 30000,
    "disponible": True
}


##Acceder a mi diccionario
print(carros["color"]) ##imprimo el diccionario para ver su contenido

##modificar valor de una clave
carros["marca"]="toyota" ##primero llamo el nombre de mi diccionario y luego la clave que quiero modificar, luego le asigno el nuevo valor
print(carros) ##imprimo el diccionario para ver el cambio

##eliminar una clave
del carros["kilometraje"] ##llamo el nombre del diccionario y la clave que quiero eliminar
print(carros) ##imprimo el diccionario para ver el cambio

##agregar una clave
carros["transmision"]="automatico" ##llamo el nombre del diccionario y le asigno la nueva clave y su valor
print(carros) ##imprimo el diccionario para ver el cambio

############################METODOS######################################

##METODO LEN
print(len(carros)) ##imprimo el diccionario para ver la cantidad de claves que tiene    

##METODO KEY
print(carros.keys()) ##imprimo el diccionario para ver las claves

##METODO VALUES
print(carros.values()) ##imprimo el diccionario para ver los valores

##METODO ITEMS
print(carros.items()) ##imprimo el diccionario para ver las claves y los valores

##METODO GET            
print(carros.get("modelo", "DATO NO ENCONTRADO")) ## el primer parametro es el dato a buscar, y el segundo es dado el caso de que no se encuentre me sale ese valor por defectol
##imprimo el diccionario para ver el valor de la clave marca

##METODO POP    
print(carros.pop("modelo", "DATO NO ENCONTRADO")) ##elimina la clave y el valor de la clave que le indico, y me devuelve el valor eliminado
print(carros) ##imprimo el diccionario para ver el cambio

##METODO POPITEM
print(carros.popitem()) ##elimina la ultima clave y el valor de la clave que le indico, y me devuelve el valor eliminado
print(carros) ##imprimo el diccionario para ver el cambio

##METODO CLEAR
carros.clear() ##elimina todas las claves y valores del diccionario
print(carros) ##imprimo el diccionario para ver el cambio

##METODO COPY
carros2=carros.copy() ##copia el diccionario
print(carros2) ##imprimo el diccionario para ver el cambio
carros2["marca"]="toyota" ##modifico el diccionario copiado
print(carros2) ##imprimo el diccionario para ver el cambio




