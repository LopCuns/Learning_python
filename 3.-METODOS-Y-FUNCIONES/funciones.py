# Las funciones nos permiten simplificar nuestro código y hacerlo más limpio ordenado y repetible de manera que nuestro código quede libre de redundancias innecesarias
# La sintaxis es la siguiente:

# def nombre(parámetros):
#   código a ejecutar

# En este ejemplo tenemos el caso de una función que recoje como input dos números y retorna su suma
def suma(numero1,numero2):
    return numero1 + numero2

print(suma(2,3))


def check_peer(numlist):
    check = [num % 2 == 0 for num in numlist ]
    return list(zip(check,numlist))
 

print(check_peer([1,2,3,4,5,6,7,8,9,10]))