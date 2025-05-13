
variable="hola mundo"
variable1= "35"

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
var=variable.isspace()
print(var)

#count(sub)	Cuenta las apariciones de un substring.	"banana".count("a") → 3
var=variable.count("a")
print(var)

#zfill(width)	Rellena el string con ceros a la izquierda hasta un ancho dado.	"42".zfill(5) → "00042"
var=variable1.zfill(5)
print(var)

#swapcase()	Invierte mayúsculas por minúsculas y viceversa.	"Hola".swapcase() → "hOLA"
var=variable.swapcase()
print(var)

#center(width)	Centra el string en un ancho determinado, rellenando con espacios.	"hi".center(5) → " hi "
var=variable.center(5)
print(var)

#ljust(width)	Alinea a la izquierda, rellenando con espacios a la derecha.	"hi".ljust(5) → "hi   "
var=variable.ljust(5)
print(var)

#rjust(width)	Alinea a la derecha, rellenando con espacios a la izquierda.	"hi".rjust(5) → "   hi"
var=variable.rjust(5)
print(var)

#partition(sep)	Divide el string en una tupla de tres partes: antes, el separador y después.	"hola mundo".partition(" ") → ("hola", " ", "mundo")
var=variable.partition(" ")
print(var) #('hola', ' ', 'mundo')

