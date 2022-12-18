# Los sets son colecciones únicas(solo puede contener un elemento una vez) y desordenadas

mi_set = set()

# Para añadir valores a un set usamos la función add() // add() solo admite un parámetro

mi_set.add(1)
mi_set.add(4)

# Para remover elementos de un set usamos la función remove()// remove() solo admite un parámetro

mi_set.remove(1)

print(mi_set)

# Podemos hacer un set a partir de una lista

mi_num_set = set([1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5])

print(mi_num_set)