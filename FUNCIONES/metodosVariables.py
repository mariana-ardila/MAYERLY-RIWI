
variable="hola mundo"

#capitalize()	Convierte el primer carácter a mayúscula.	"hola mundo" → "Hola mundo"
var=variable.capitalize()
print(var)

#lower()	Convierte todos los caracteres en minúscula.	"PYTHON" → "python"
var=variable.lower()
print(var)

#upper()	Convierte todos los caracteres en mayúscula.	"python" → "PYTHON"
var=variable.upper()
print(var)

#title()	Convierte el primer carácter de cada palabra a mayúscula.	"hola mundo" → "Hola Mundo"
var=variable.title()
print(var)

#strip()	Elimina espacios (u otros caracteres) al principio y final.	" hola " → "hola"
var=variable.strip()
print(var)

#lstrip()	Elimina espacios al inicio.	" hola" → "hola"
var=variable.lstrip()
print(var)

#rstrip()	Elimina espacios al final.	"hola " → "hola"
var=variable.rstrip()
print(var)

#replace(old, new)	Reemplaza un substring por otro.	"hola mundo" → "hola gente"
var=variable.replace("hola mundo", "hola maye")
print(var)

#find(sub)	Devuelve el índice de la primera aparición, o -1 si no existe.	"Hola Mundo".find("Mundo") → 5
var=variable.find("mundo")
print(var)

#rfind(sub)	Igual que find, pero buscando desde el final.	"abracadabra".rfind("abra") → 7
var=variable.rfind("hola")
print(var)

#split(sep)	Divide el string en una lista usando el separador.	"a,b,c".split(",") → ["a", "b", "c"]
var=variable.split("-")
print(var)

#join(iterable)	Une los elementos de un iterable usando el string como separador.	",".join(["a", "b", "c"]) → "a,b,c"
var=variable.join(",")
print(var)

#startswith(sub)	Retorna True si inicia con el substring dado.	"hola mundo".startswith("hola") → True
var=variable.startswith("hola")
print(var)

#endswith(sub)	Retorna True si termina con el substring dado.	"archivo.txt".endswith(".txt") → True
var=variable.endswith("maye")
print(var)

#isalpha()	Retorna True si todos los caracteres son letras.	"Python".isalpha() → True
var=variable.isalpha()
print(var)

#isdigit()	Retorna True si todos los caracteres son números.	"12345".isdigit() → True
var=variable.isdigit()
print(var)

#isalnum()	Retorna True si todos los caracteres son alfanuméricos.	"abc123".isalnum() → True
var=variable.isalnum()
print(var)
#isspace()	Retorna True si solo contiene espacios.	" ".isspace() → True
#count(sub)	Cuenta las apariciones de un substring.	"banana".count("a") → 3
#zfill(width)	Rellena el string con ceros a la izquierda hasta un ancho dado.	"42".zfill(5) → "00042"
#swapcase()	Invierte mayúsculas por minúsculas y viceversa.	"Hola".swapcase() → "hOLA"
#center(width)	Centra el string en un ancho determinado, rellenando con espacios.	"hi".center(5) → " hi "