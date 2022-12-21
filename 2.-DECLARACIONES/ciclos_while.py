# Los ciclos while ejecutan un fragmento de código mientras una condición sea verdadera

x = 0


while x<=5:
    print(f"el valor de x es {x}")
    x+=1
else:
    print('x es mayor a 5')


# pass,continue y break en bucles

lista = [1,2,3,4,5,6]

for item in lista:
    # podemos usar pass cuando temporalmente una declaración(cilco for,while,if,elif,else...) no tengan contenido
    pass

y = 0

while y<=5:
    if y==3:
        break # con break rompemos el ciclo, es decir, no hará más iteraciones ni se ejecutará el codigo contenido por el mismo después de esta palabra clave.
    print(y)
    y+=1


for item in lista:
    if item==3:
        continue #con continue nos saltamos la iteración actual, es decir, no se ejecutará el código contenido después de esta palabra clave en dicha iteración y se pasará a la siguiente
    print(item)
