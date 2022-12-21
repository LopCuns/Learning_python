# Los ciclos for pueden iterar listas,cadenas de texto y diccionarios

cadena = 'Hola mundo'
lista = [1,2,3,4,5,6,7,8,9,10]
diccionario = {'y1':1,'y2':2,'y3':3}

for char in cadena:
    print(char)

for num in lista:
    print(num)

for key in diccionario:
    print(key)  #Al iterar sobre los diccionarios el valor de la variable será la llave


# TÉCINCA DEL TUPLE UNPACKING
# Replicando la estructura de una tupla con nombres de variables, podemos hacer que el valor en su posición sea el valor de la tupla

(t1,t2,t3,t4,t5) = (1,2,3,4,5)

print(t1,t2,t3,t4,t5)

# Esto podemos aplicarlo a los ciclos for ,por ejemplo,para iterar sobre los pares llave-valor de un diccionario

for (llave,valor) in diccionario.items():
    print(f'La llave es {llave} y su valor es {valor}')