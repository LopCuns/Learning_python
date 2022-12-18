# Indices----------->0  1  2  3  4  5...
#Indices negativos-->0 -1 -2 -3 -4 -5...

my_string = "comillas dobles"

my_second_string = 'comillas simples'

my_final_string = "Cadena's con comillas dentro '''\n'''"

print(my_final_string,len(my_final_string))


# SLICING

#Slice ---> cadena[start:stop:step]
#.-start-->primer caracter recogido
#.-stop -->primer caracter no recogido
#.-step --> salto entre caracteres

ejemplo_cadena = "abcdefghijklmnopqrstuvwxyz"

print(ejemplo_cadena[0:2],ejemplo_cadena[0:10:3],ejemplo_cadena[-6:-1],ejemplo_cadena[::])


# PROPIEDADES Y MÉTODOS


# Las cadenas son *inmutables*, lo que quiere decir que una vez creadas no podrán ser modificadas
# Para "modificar" una string podemos usar el slicing de la siguiente manera
my_str = "no,unmodified string"
my_mod_str = "yes," + my_str[5:]
print(my_mod_str)

#Multiplicar una cadena de texto
letra = 'z' 

print(letra * 3)

# metodos importantes
# upper-->pone las letras en mayúsculas
# lower-->pone las letras en minúsculas
# split--> separa la string en una lista según el espaciador indicado

text = "AbCd EfGh IjK"
text2 = "hola|mundo|slipt"
print(text.lower(),text.upper(),text.split(),text2.split("|"))



# FORMATEAR UNA STRING
# Funcion .format de las strings
# añadirá el valor pasado como parámetro sustituyendo a {} de las siguientes maneras
print("esta es una cadena de texto con valores añadidos : {}".format('valor añadido_1'))
print("esta es una cadena de texto con valores añadidos : {0} {0} {0}".format('valor añadido_1','valor añadido_2'))
print("esta es una cadena de texto con valores añadidos : {0} {1} {2}".format('valor añadido_1','valor añadido_2','valor añadido_3'))
print("esta es una cadena de texto con valores añadidos : {v1} {v2} {v3}".format(v1 = 'valor añadido_1',v2 = 'valor añadido_2',v3 = 'valor añadido_3'))

# con floats
math_pi = 3.1415926535897932384626433832795
# Formateo de float {var:(width).(precisión)f}
print("el número pi equivale a : {pi:1.5f}".format(pi = math_pi))


# F strings
# Hace lo mismo que la función format pero de una forma más clara y legible

# Sintaxis ---> f"cadena de texto {valor o variable añadid@}" (ver en el ejemplo de abajo)

valor_añadido = "valor añadido por variable"
print(f"ejemplo de f string,añadido : {valor_añadido} , {'valor añadido directamente'}")





print('LopCuns')