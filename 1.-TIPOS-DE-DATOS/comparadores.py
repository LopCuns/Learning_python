# Los comparadores de operación devuelven True o False al evaluar una condición
# Los comparadores de operación son:
# == (igual)
# != (distinto de)
# > (mayor a)
# < (menor a)
# >= (mayor o igual a)
# <= (menor o igual a)

print("Hola" == 'Hola',2 == 3)
print(3 != 2, "2" != 2)
print(3 > 2,2 < 1)
print(2>=2, 2>=3)
print(2<=1, 2<=3)


# Los comparadores de concatenación nos permiten unir diferentes comparaciones lógicas
# Los comparadores de concatenación son:
# and (y) será verdadero cuando todas las condiciones sean verdaderas, en caso contrario será falso
# or (o) será verdadero si al menos una de las condiciones es verdadera.Solo si todas las condiciones son falsas será falso
# not (no) devuelve el booleano opuesto a una comparación


print(2>1 and 3<1,2>1 and 3>2)

print(2<1 or 3>2, 2<1 or 3<2)

print(not 1==1,not 2<3)