from random import shuffle,randint


# Operador range
# Crea un rango comprendido entre el número indicado como primer parámetro y el indicado en el segundo parámetro(sin incluir) con un incremento del tercer parámetro

print(list(range(2,10,2)))


# Operador enumerate
# Enumera los carácteres de una cadena de texto creando una tupla con su indice
palabra = 'palabra'
print(list(enumerate(palabra)))


# Operador zip
# Crea una tupla que auna los componentes de diferentes listas que comparten un mismo índice hasta el máximo de la lista más corta
lista_1 = [1,2,3,4,5,6,7,8]
lista_2 = [100,200,300,400,500]
lista_3 = ['uno','dos','tres','cuatro','cinco']

# A pesar de que la lista_1 tenga 8 elementos, a partir del 5 ninguno aparece en el zip porque el máximo de la más corta (lista_2 y lista_3) es 5
print(list(zip(lista_1,lista_2,lista_3)))


# Operador in
# Devuelve un booleano indicando si un elemento está presente en algún contenedor(lista,cadena de texto,diccionario,tupla...)

lista = [1,2,3,4,5]

print(1 in lista,10 in lista)

# Operadores max y min
# max devuelve el valor más alto de un conjunto de valores
# min devuelve el valor más bajo de un conjunto de valores
dic = {'k1':1,'k2':2,'k3':3,'k4':4,'k5':5,'k6':6,'k7':7,'k8':8,'k9':9,'k10':10}
print(max(dic.values()),min(dic.values()))


# shuffle (random)
# desordena un conjunto de valores

shuffle(lista)
print(lista)

# randint (random)
# devuelve un entero aleatorio comprendido entre dos enteros

print(randint(1,100))


# input
# le pide al usuario que ingrese un valor

tel_num = input('Ingrese su número de teléfono:  ')
mail_direction = input('Ingrese su correo electrónico:  ')
print(f"su número de teléfono es:{tel_num} y su dirección de correo electrónico es:{mail_direction}")


