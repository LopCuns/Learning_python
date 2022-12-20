# if, elif y else son declaraciones que nos permiten controlar el flujo de nuestro programa
# Funcionan como en el resto de lenguajes de programación
# Para entender el funcionamiento ver el siguiente ejemplo
hambre = False
sed = False

if hambre and sed:
    print('Tengo hambre y sed')
elif hambre and not sed:
    print('Tengo hambre')
elif not hambre and sed:
    print('Tengo sed')
else:
    print('Estoy full')


# Ternary operator
# Nos permite simplificar una estructura simple de if else
# Sintaxis (valor si falso,valor si verdadero)[condición]
# Veamos el siguiente ejemplo:

print(("No tengo hambre","Tengo hambre")[hambre])

# MOTA: el ternary operator solo sirve para devolver valores no para devolver la ejecución de una función, por ejemplo:
# (print("No tengo hambre"),print("Tengo hambre"))[hambre]
# este ejemplo no funcionará correctamente.


#Condiciones con diccionarios

# Una manera más vistosa y sencilla de escribir condiciones largas es usando diccionarios de la siguiente manera

day ="domingo"


condicion_dias = {
    'LUNES':"Hoy es Lunes, que pereza ir al trabajo :(",
    'MARTES':"Aún es Martes, todavía queda mucho para el fin de semana ;(",
    'MIÉRCOLES':"Ánimo que ya es Miércoles y ya estamos a mitad de semana!!!",
    'JUEVES':"Ya es Jueves, no queda casi nada para el fin de semana",
    'VIERNES':"Hoy es Viernes y tu cuerpo LO SABE :))))))",
    'SÁBADO':"Que bien sienta el café un Sábado por la mañana",
    'DOMINGO':"Ya es Domingo... a disfrutar de lo que queda de descanso"
}

print(condicion_dias[day.upper()])
# Aquí le dicemos que busque en el diccionario la llave con el valor de la variable day y nos devuelva su contenido