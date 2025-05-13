#sum(iterable)	Suma todos los elementos de un iterable.	sum([1, 2, 3]) → 6
#len(iterable)	Longitud de un iterable.	len("hola") → 4
#sorted(iterable)	Ordena un iterable.	sorted([3, 1, 2]) → [1, 2, 3]
#reversed(iterable)	Invierte un iterable.	reversed([1, 2, 3]) → [3, 2, 1]
#all(iterable)	Retorna True si todos los elementos son verdaderos.	all([True, True]) → True
#any(iterable)	Retorna True si al menos un elemento es verdadero.	any([False, True]) → True
#enumerate(iterable)	Retorna un iterable de tuplas (índice, valor).	enumerate(["a", "b"]) → [(0, "a"), (1, "b")]
#map(func, iterable)	Aplica una función a cada elemento de un iterable.	map(str, [1, 2, 3]) → ["1", "2", "3"]
#filter(func, iterable)	Filtra elementos de un iterable según una función.	filter(lambda x: x > 0, [-1, 0, 1]) → [1]
#zip(*iterables)	Combina elementos de varios iterables.	zip([1, 2], ["a", "b"]) → [(1, "a"), (2, "b")]
#reduce(func, iterable)	Aplica una función acumulativa a los elementos de un iterable.	reduce(lambda x, y: x + y, [1, 2, 3]) → 6
