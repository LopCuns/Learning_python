# Con la técnica de las listas de comprensión podemos hacer una lista a partir de otra modificando los valores de la primera en la segunda

celsius = [0,34,50,25,89]
kelvin = [temp + 273 for temp in celsius]

cuadrados_pares = [num**2 for num in range(1,11)]

print(kelvin,cuadrados_pares)