# Las tuplas funcionan igual que las listas pero con la diferencia de que estas son inmutables mientras que las listas son mutables, es decir, no podemos modificar el contenido de las tuplas
# Las tuplas tienen indices(positivos y negativos) al igual que las listas y también admiten slicing

tupla = ('a','b','c','a','a','b')

print(tupla)

print(tupla[1:],tupla[0:-1])

# Podemos usar la función count() para contar el número de veces que se repite un elemento en la tupla

print(tupla.count('a'),tupla.count('b'))

# Podemos usar la función index() para recoger el primer índice de un elemento en la tupla

print(tupla.index('b'))
