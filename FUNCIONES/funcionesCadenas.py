#FUNCIONES DE CADENAS
# Función para contar el número de vocales en una cadena
def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in 'aeiouáéíóú':
            contador += 1
    return contador

# Función para contar el número de consonantes en una cadena
def contar_consonantes(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in 'bcdfghjklmnpqrstvwxyz':
            contador += 1
    return contador

# Función para contar el número de palabras en una cadena
def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

# Función para contar el número de caracteres en una cadena
def contar_caracteres(cadena):
    return len(cadena)

# Función para contar el número de espacios en una cadena
def contar_espacios(cadena):
    contador = 0
    for letra in cadena:
        if letra == ' ':
            contador += 1
    return contador

# Función para contar el número de caracteres especiales en una cadena
def contar_caracteres_especiales(cadena):
    contador = 0
    for letra in cadena:
        if not letra.isalnum() and letra != ' ':
            contador += 1
    return contador

# Función para contar el número de mayúsculas en una cadena
def contar_mayusculas(cadena):
    contador = 0
    for letra in cadena:
        if letra.isupper():
            contador += 1
    return contador

# Función para contar el número de minúsculas en una cadena
def contar_minusculas(cadena):
    contador = 0
    for letra in cadena:
        if letra.islower():
            contador += 1
    return contador

# Función para contar el número de dígitos en una cadena
def contar_digitos(cadena):
    contador = 0
    for letra in cadena:
        if letra.isdigit():
            contador += 1
    return contador

# Función para contar el número de caracteres únicos en una cadena
def contar_caracteres_unicos(cadena):
    return len(set(cadena))
# Función para contar el número de caracteres repetidos en una cadena
def contar_caracteres_repetidos(cadena):
    contador = 0
    for letra in set(cadena):
        if cadena.count(letra) > 1:
            contador += 1
    return contador

# Función para contar el número de palabras únicas en una cadena
def contar_palabras_unicas(cadena):
    return len(set(cadena.split()))
# Función para contar el número de palabras repetidas en una cadena
def contar_palabras_repetidas(cadena):
    contador = 0
    for palabra in set(cadena.split()):
        if cadena.split().count(palabra) > 1:
            contador += 1
    return contador

# Función para contar el número de oraciones en una cadena
def contar_oraciones(cadena):
    return cadena.count('.') + cadena.count('!') + cadena.count('?')

# Función para contar el número de párrafos en una cadena
def contar_parrafos(cadena):
    return cadena.count('\n') + 1

# Función para contar el número de líneas en una cadena
def contar_lineas(cadena):
    return cadena.count('\n') + 1

# Función para contar el número de caracteres en una cadena sin espacios
def contar_caracteres_sin_espacios(cadena):
    return len(cadena.replace(' ', ''))

# Función para contar el número de caracteres en una cadena sin dígitos
def contar_caracteres_sin_digitos(cadena):
    return len(cadena.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', ''))

# Función para contar el número de caracteres en una cadena sin mayúsculas
def contar_caracteres_sin_mayusculas(cadena):
    return len(cadena.replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', ''))

# Función para contar el número de caracteres en una cadena sin minúsculas
def contar_caracteres_sin_minusculas(cadena):
    return len(cadena.replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', ''))

# Función para contar el número de caracteres en una cadena sin caracteres especiales           
def contar_caracteres_sin_caracteres_especiales(cadena):
    return len(cadena.replace('!', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('(', '').replace(')', '').replace('-', '').replace('_', '').replace('=', '').replace('+', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(':', '').replace(';', '').replace('"', '').replace("'", '').replace('<', '').replace('>', '').replace(',', '').replace('.', ''))

# Función para contar el número de caracteres en una cadena sin espacios y sin dígitos
def contar_caracteres_sin_espacios_y_digitos(cadena):
    return len(cadena.replace(' ', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', ''))

# Función para contar el número de caracteres en una cadena sin espacios y sin mayúsculas
def contar_caracteres_sin_espacios_y_mayusculas(cadena):
    return len(cadena.replace(' ', '').replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', ''))

# Función para contar el número de caracteres en una cadena sin espacios y sin minúsculas
def contar_caracteres_sin_espacios_y_minusculas(cadena):
    return len(cadena.replace(' ', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', ''))

# Función para contar el número de caracteres en una cadena sin espacios y sin caracteres especiales        
def contar_caracteres_sin_espacios_y_caracteres_especiales(cadena):
    return len(cadena.replace(' ', '').replace('!', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('(', '').replace(')', '').replace('-', '').replace('_', '').replace('=', '').replace('+', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(':', '').replace(';', '').replace('"', '').replace("'", '').replace('<', '').replace('>', '').replace(',', '').replace('.', ''))

# Función para contar el número de caracteres en una cadena sin dígitos y sin mayúsculas
def contar_caracteres_sin_digitos_y_mayusculas(cadena):
    return len(cadena.replace('A', '').replace('B', '').replace('C', '').replace('D', '').replace('E', '').replace('F', '').replace('G', '').replace('H', '').replace('I', '').replace('J', '').replace('K', '').replace('L', '').replace('M', '').replace('N', '').replace('O', '').replace('P', '').replace('Q', '').replace('R', '').replace('S', '').replace('T', '').replace('U', '').replace('V', '').replace('W', '').replace('X', '').replace('Y', '').replace('Z', ''))

# Función para contar el número de caracteres en una cadena sin dígitos y sin minúsculas
def contar_caracteres_sin_digitos_y_minusculas(cadena):
    return len(cadena.replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', ''))
