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



