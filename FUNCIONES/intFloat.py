numeros=1,2,3,4,5,6,7,8,9,10
string="2"
floatt="3.14"

#abs(x)	Valor absoluto.	abs(-7) → 7
num=abs(-7)
print(num)

#max(x)	Valor máximo.	max(1, 2, 3) → 3
num=max(1,2,3)
print(num)

#min(x)	Valor mínimo.	min(1, 2, 3) → 1
num=min(1,2,3)
print(num)

#round(x)	Redondea al entero más cercano.	round(4.6) → 5
num_rounded=round(4.6)
print(num_rounded)

#pow(x, y)	Potencia x elevado a y.	pow(2, 3) → 8
num_pow=pow(2,3)
print(num_pow)

#int(x)	Convierte a entero.	int("12") → 12
num_int=int(string)
print(num_int)

#float(x)	Convierte a decimal.	float("3.14") → 3.14
num_float=float(floatt)
print(num_float)

#str(x)	Convierte a string.	str(12) → "12"
num_str=str(num_int)
print(num_str)

#type(x)	Retorna el tipo de dato.	type(3.14) → <class 'float'>
num_type=type(num_float)
print(num_type)

#isinstance(x, y)	Verifica si x es instancia de y.	isinstance(3, int) → True
num_isinstance=isinstance(num_int, int)
print(num_isinstance)

#suma(x, y)	Suma dos números.	suma(2, 3) → 5
def suma(x, y):
    return x + y
num_suma=suma(2,3)
print(num_suma)

#resta(x, y)	Resta dos números.	resta(5, 3) → 2
def resta(x, y):
    return x - y
num_resta=resta(5,3)
print(num_resta)

#multiplicacion(x, y)	Multiplica dos números.	multiplicacion(2, 3) → 6
def multiplicacion(x, y):
    return x * y
num_multiplicacion=multiplicacion(2,3)
print(num_multiplicacion)

#division(x, y)	Divide dos números.	division(6, 3) → 2.0    
def division(x, y):
    return x / y
num_division=division(6,3)
print(num_division)

#modulo(x, y)	Retorna el residuo de la división.	modulo(5, 2) → 1
def modulo(x, y):
    return x % y
num_modulo=modulo(5,2)
print(num_modulo)

#potencia(x, y)	Retorna x elevado a y.	potencia(2, 3) → 8
def potencia(x, y):
    return x ** y
num_potencia=potencia(2,3)
print(num_potencia)

#raiz(x)	Retorna la raíz cuadrada.	raiz(16) → 4.0
def raiz(x):
    return x ** 0.5
num_raiz=raiz(16)
print(num_raiz)

#logaritmo(x, base)	Retorna el logaritmo de x en la base dada.	logaritmo(100, 10) → 2.0
import math
def logaritmo(x, base):
    return math.log(x, base)
num_logaritmo=logaritmo(100, 10)
print(num_logaritmo)

#factorial(x)	Retorna el factorial de x.	factorial(5) → 120
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
num_factorial=factorial(5)
print(num_factorial)

#combinacion(n, k)	Retorna el número de combinaciones de n elementos tomados de k en k.	combinacion(5, 2) → 10
def combinacion(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
num_combinacion=combinacion(5, 2)
print(num_combinacion)

#permutacion(n, k)	Retorna el número de permutaciones de n elementos tomados de k en k.	permutacion(5, 2) → 20
def permutacion(n, k):
    return factorial(n) // factorial(n - k)
num_permutacion=permutacion(5, 2)
print(num_permutacion)

#esPrimo(x)	Verifica si x es un número primo.	esPrimo(7) → True
def esPrimo(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
num_esPrimo=esPrimo(7)
print(num_esPrimo)

#esPar(x)	Verifica si x es un número par.	esPar(4) → True
def esPar(x):
    return x % 2 == 0
num_esPar=esPar(4)  
print(num_esPar)

#esImpar(x)	Verifica si x es un número impar.	esImpar(5) → True
def esImpar(x):
    return x % 2 != 0
num_esImpar=esImpar(5)
print(num_esImpar)

#esPositivo(x)	Verifica si x es un número positivo.	esPositivo(3) → True
def esPositivo(x):
    return x > 0
num_esPositivo=esPositivo(3)
print(num_esPositivo)

#esNegativo(x)	Verifica si x es un número negativo.	esNegativo(-3) → True
def esNegativo(x):
    return x < 0
num_esNegativo=esNegativo(-3)
print(num_esNegativo)


#esCero(x)	Verifica si x es cero.	esCero(0) → True
def esCero(x):
    return x == 0
num_esCero=esCero(0)
print(num_esCero)

#numerosPrimosHasta(n)	Retorna una lista de números primos hasta n.	numerosPrimosHasta(10) → [2, 3, 5, 7]
def numerosPrimosHasta(n):
    primos = []
    for i in range(2, n + 1):
        if esPrimo(i):
            primos.append(i)
    return primos
num_numerosPrimosHasta=numerosPrimosHasta(10)
print(num_numerosPrimosHasta)

#numerosParesHasta(n)	Retorna una lista de números pares hasta n.	numerosParesHasta(10) → [0, 2, 4, 6, 8, 10]
def numerosParesHasta(n):
    return [i for i in range(n + 1) if esPar(i)]
num_numerosParesHasta=numerosParesHasta(10)
print(num_numerosParesHasta)

#numerosImparesHasta(n)	Retorna una lista de números impares hasta n.	numerosImparesHasta(10) → [1, 3, 5, 7, 9]
def numerosImparesHasta(n):
    return [i for i in range(n + 1) if esImpar(i)]
num_numerosImparesHasta=numerosImparesHasta(10)
print(num_numerosImparesHasta)  

#numerosPositivosHasta(n)	Retorna una lista de números positivos hasta n.	numerosPositivosHasta(10) → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def numerosPositivosHasta(n):
    return [i for i in range(1, n + 1)]
num_numerosPositivosHasta=numerosPositivosHasta(10)
print(num_numerosPositivosHasta)

#numerosNegativosHasta(n)	Retorna una lista de números negativos hasta n.	numerosNegativosHasta(-10) → [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
def numerosNegativosHasta(n):
    return [i for i in range(-1, n - 1, -1)]
num_numerosNegativosHasta=numerosNegativosHasta(-10)
print(num_numerosNegativosHasta)

#numerosCerosHasta(n)	Retorna una lista de ceros hasta n.	numerosCerosHasta(10) → [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def numerosCerosHasta(n):
    return [0 for i in range(n + 1)]
num_numerosCerosHasta=numerosCerosHasta(10)
print(num_numerosCerosHasta)

#numerosAleatoriosHasta(n)	Retorna una lista de números aleatorios hasta n.	numerosAleatoriosHasta(10) → [3, 7, 1, 9, 2]
import random
def numerosAleatoriosHasta(n):
    return [random.randint(1, n) for i in range(n)]
num_numerosAleatoriosHasta=numerosAleatoriosHasta(10)
print(num_numerosAleatoriosHasta)

#numerosFibonacciHasta(n)	Retorna una lista de números de Fibonacci hasta n.	numerosFibonacciHasta(10) → [0, 1, 1, 2, 3, 5, 8]
def numerosFibonacciHasta(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]
num_numerosFibonacciHasta=numerosFibonacciHasta(10)
print(num_numerosFibonacciHasta)

#numerosFactorialesHasta(n)	Retorna una lista de números factoriales hasta n.	numerosFactorialesHasta(5) → [1, 1, 2, 6, 24, 120]
def numerosFactorialesHasta(n):
    fact = [factorial(i) for i in range(n + 1)]
    return fact
num_numerosFactorialesHasta=numerosFactorialesHasta(5)
print(num_numerosFactorialesHasta)

#numerosCuadradosHasta(n)	Retorna una lista de números cuadrados hasta n.	numerosCuadradosHasta(5) → [0, 1, 4, 9, 16, 25]
def numerosCuadradosHasta(n):
    cuadrados = [i ** 2 for i in range(n + 1)]
    return cuadrados
num_numerosCuadradosHasta=numerosCuadradosHasta(5)
print(num_numerosCuadradosHasta)

#numerosCubicosHasta(n)	Retorna una lista de números cúbicos hasta n.	numerosCubicosHasta(5) → [0, 1, 8, 27, 64, 125]
def numerosCubicosHasta(n):
    cubicos = [i ** 3 for i in range(n + 1)]
    return cubicos
num_numerosCubicosHasta=numerosCubicosHasta(5)
print(num_numerosCubicosHasta)

#---------------------------------------------------------------------------------------------------------------------------------------------
#ESTADISTICAS

#porcentaje(x, y)	Retorna el porcentaje de x respecto a y.	porcentaje(20, 100) → 20.0
def porcentaje(x, y):
    return (x / y) * 100
num_porcentaje=porcentaje(20, 100)
print(num_porcentaje)

#promedio(lista)	Retorna el promedio de una lista.	promedio([1, 2, 3]) → 2.0
def promedio(lista):
    return sum(lista) / len(lista)
num_promedio=promedio([1, 2, 3])
print(num_promedio)

#desviacionEstandar(lista)	Retorna la desviación estándar de una lista.	desviacionEstandar([1, 2, 3]) → 0.816496580927726
def desviacionEstandar(lista):
    prom = promedio(lista)
    return (sum((x - prom) ** 2 for x in lista) / len(lista)) ** 0.5
num_desviacionEstandar=desviacionEstandar([1, 2, 3])
print(num_desviacionEstandar)

#varianza(lista)	Retorna la varianza de una lista.	varianza([1, 2, 3]) → 0.6666666666666666
def varianza(lista):
    prom = promedio(lista)
    return sum((x - prom) ** 2 for x in lista) / len(lista)
num_varianza=varianza([1, 2, 3])
print(num_varianza)

#covarianza(lista1, lista2)	Retorna la covarianza entre dos listas.	covarianza([1, 2, 3], [4, 5, 6]) → 0.6666666666666666
def covarianza(lista1, lista2):
    prom1 = promedio(lista1)
    prom2 = promedio(lista2)
    return sum((x - prom1) * (y - prom2) for x, y in zip(lista1, lista2)) / len(lista1)
num_covarianza=covarianza([1, 2, 3], [4, 5, 6])
print(num_covarianza)

#correlacion(lista1, lista2)	Retorna la correlación entre dos listas.	correlacion([1, 2, 3], [4, 5, 6]) → 0.9999999999999999
def correlacion(lista1, lista2):
    cov = covarianza(lista1, lista2)
    desv1 = desviacionEstandar(lista1)
    desv2 = desviacionEstandar(lista2)
    return cov / (desv1 * desv2)
num_correlacion=correlacion([1, 2, 3], [4, 5, 6])
print(num_correlacion)

#moda(lista)	Retorna la moda de una lista.	moda([1, 2, 2, 3]) → 2
from collections import Counter
def moda(lista):
    return Counter(lista).most_common(1)[0][0]
num_moda=moda([1, 2, 2, 3])
print(num_moda)

#mediana(lista)	Retorna la mediana de una lista.	mediana([1, 2, 3]) → 2
def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        return lista[n // 2]
num_mediana=mediana([1, 2, 3])
print(num_mediana)

#rango(lista)	Retorna el rango de una lista.	rango([1, 2, 3]) → 2
def rango(lista):
    return max(lista) - min(lista)
num_rango=rango([1, 2, 3])
print(num_rango)

#cuartiles(lista)	Retorna los cuartiles de una lista.	cuartiles([1, 2, 3]) → (1.5, 2.0, 2.5)
def cuartiles(lista):
    lista.sort()
    n = len(lista)
    q1 = mediana(lista[:n // 2])
    q2 = mediana(lista)
    q3 = mediana(lista[n // 2 + 1:] if n % 2 == 0 else lista[n // 2 + 1:])
    return q1, q2, q3
num_cuartiles=cuartiles([1, 2, 3])
print(num_cuartiles)

#percentiles(lista, p)	Retorna el percentil p de una lista.	percentiles([1, 2, 3], 50) → 2.0
def percentiles(lista, p):
    lista.sort()
    n = len(lista)
    k = (n - 1) * p / 100
    f = int(k)
    c = k - f
    if f + 1 < n:
        return lista[f] + c * (lista[f + 1] - lista[f])
    else:
        return lista[f]
num_percentiles=percentiles([1, 2, 3], 50)
print(num_percentiles)

#histograma(lista)	Retorna un histograma de una lista.	histograma([1, 2, 2, 3]) → {1: 1, 2: 2, 3: 1}
def histograma(lista):
    hist = {}
    for i in lista:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1
    return hist
num_histograma=histograma([1, 2, 2, 3])
print(num_histograma)
#---------------------------------------------------------------------------------------------------------------------------------------------



