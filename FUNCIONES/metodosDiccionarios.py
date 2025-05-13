usuario={
    "nombre":"Juan",
    "edad":30,
    "ciudad":"Madrid"}

#get() Retorna el valor asociado a la clave, o None.
usuario.get("nombre")
print(usuario.get("nombre")) 

#keys()	Retorna una vista de las claves.	
usuario.keys()
print(usuario.keys())

#values()	Retorna una vista de los valores.	
usuario.values()
print(usuario.values())


#items()	Retorna una vista de los pares clave-valor.	
usuario.items()
print(usuario.items())

#pop(k)	Elimina la clave y retorna su valor.
print(usuario.pop("edad"))  

#popitem()	Elimina el último par insertado.	datos.popitem()
print(usuario.popitem())

#update(other)	Actualiza con pares clave-valor de otro dict.	perfil.update({"email": "a@b.com"})
print(usuario.update({"nombre": "Juan"}))

#clear()	Elimina todos lo Retorna el valor asociado a la clave, o None.s elementos.	datos.clear()
print(usuario.clear())

#setdefault(k,v)	Retorna valor si existe, si no, lo asigna.	config.setdefault("modo", "oscuro")
print(usuario.setdefault("nombre", "Juan"))

#copy()	Retorna una copia superficial.	nuevo = original.copy()
print(usuario.copy())
