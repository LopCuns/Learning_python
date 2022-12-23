# map
# Nos permite aplicarle una función a todos los elementos de una lista

list_num = [1,2,3,4,5,6,7,8,9,10]
def square(num):
    return num**2
print(list(map(square,list_num)))

# filter
# permite filtrar una lista con aquellos valores que se cumplan para una función

def check_odd(num):
    return not(num % 2 == 0)

print(list(filter(check_odd,list_num)))

# palabra reservada lambda
# nos permite simplificar funciones en las que no necesitemos escribir mucho código o solo querramos una operación sobre un valor

# Por ejemplo, las funciones check_odd y square de arriba podrían simplificarse de la siguiente manera

lambda_square = lambda num: num**2 
lambda_check_odd = lambda num : not(num % 2 == 0)

# Y de igual manera podremos simplificar nuestros mapeos y filtros

print(list(map(lambda num:num**2,list_num)))
print(list(filter(lambda num:not(num % 2 == 0),list_num)))


# USO DE VARIABLES GLOBALES EN FUNCIONES
# Para hacer uso de variables globales en funciones y modificar sus valores sin que se creen variables locales dentro de las mismas usaremos la palabra reservada global

x = 50
y = 30
def modXY():
    global x,y
    x = 500
    y = 300
    print(f"los valores de x e y han sido modificados correctamente a {x} {y} respectivamente")

modXY()
print(x,y)
