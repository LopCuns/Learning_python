# LISTAS
# .-Son mutables(podemos alterar su contenido)
# .-Podemos recuperar la longitud de una lista con la función len()
# .-Las listas tienen indicies (positivos y negativos al igual que las cadenas de texto)
# .-Las listas admiten slicing
# .-Se pueden concatenar con el operador "+"
# .-Se les pueden añadir elementos con la función append() y remover con la función pop()
# .-Se pueden ordenar con la función sort()
# .-Se pueden revertir con la función reverse)()



mi_num_lista = [5,8,1,6,9,2,3,7,4]
mi_let_lista = ['v','c','j','h','p','e','a']

# longitud de una lista con len()

print(len(mi_let_lista))

# listas e indices (positivos y negativos)

print(mi_num_lista[3])

# Listas y slicing

print(mi_let_lista[3:])

# reemplazar elementos de una lista

mi_let_lista[4] = 'cuatro'

print(mi_let_lista)

# Concatenación de listas

print(mi_num_lista + mi_let_lista)

# añadir elementos al final de una lista con append()

mi_num_lista.append(3)
print(mi_num_lista)

# remover elementos de una lista con pop()

popped_element = mi_let_lista.pop(-3)

print(mi_let_lista,popped_element)

# ordernar una lista con sort()

unordered_list = [2,1,5,6,9,10,3,8]

unordered_list.sort()

print(unordered_list)

# revertir una lista con reverse()

unordered_list.reverse()

print(unordered_list)
