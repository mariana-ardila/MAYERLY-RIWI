

##METODOSSSSS

frutas=["mango", "sandia"]
verduras=["cebolla","tomate","zanahoria", "limon", "limon"]

##append()	Agrega un elemento al final de la lista.	Agrega "manzana" a la lista de frutas.
frutas.append("manzana")
print(frutas)

##extend()	Agrega los elementos de otra lista al final de la lista actual.	Une la lista de frutas con la de verduras.
frutas.extend(verduras)
print(frutas)

#insert()	Inserta un elemento en una posición específica.	Inserta "pera" en la posición 2 de la lista.
frutas.insert(2,"pera")
print(frutas)

#remove()	Elimina la primera ocurrencia de un valor específico.	Elimina "mango" de la lista de frutas.
frutas.remove("mango")
print(frutas)

#pop()	    Elimina y devuelve un elemento en una posición dada (o el último).	Elimina la fruta en la posicion 0 "manzana".
frutas.pop(0)
print(frutas)

#index()	Devuelve el índice de la primera aparición de un valor.	Encuentra la posición de "tomate" en la lista.
verdura=verduras.index("tomate")
print(verdura)

#count()	Cuenta cuántas veces aparece un valor en la lista.	Cuenta cuántas veces aparece "limón".
verdura=verduras.count("limon")
print(verdura)

#sort()	    Ordena los elementos de la lista (por defecto de menor a mayor).	Ordena las verduras por el abecedario
verduras.sort()
print(verduras)

#reverse()	Invierte el orden de los elementos de la lista.	Invierte una lista de nombres.
frutas.reverse()
print(frutas)

#copy()	    Devuelve una copia superficial de la lista.	Crea una copia de la lista de frutas.
frutas.copy()
print(frutas)

#clear()	Elimina todos los elementos de la lista.	Vacía completamente la lista de tareas.
frutas.clear()
print(frutas)