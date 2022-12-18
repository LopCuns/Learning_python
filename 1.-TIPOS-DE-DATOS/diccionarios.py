mi_diccionario = {
    'ordenador':"Un ordenador es un sistema conformado por programas y elementos electrónicos.",
    'manzana':"fruto de color verde que brota del manzano.",
    'libro':"conjunto de texto coherente que tiene un significado.",
    'ratón':[
        'roedor de pequeño tamaño que habita en las cloacas.',
        'dispositivo electrónico que mueve el cursor de un ordeandor.'
    ]
}

print(mi_diccionario)

# coger el valor de una clave del diccionario
print(mi_diccionario['ordenador'])

print(mi_diccionario['ratón'][1])

#añadir claves y valores a diccionarios 
mi_diccionario['regalo'] = "acción o cosa que se le entrega a alguien como muestra de afecto."

print(mi_diccionario)

# recoger las claves de un diccionario

print(mi_diccionario.keys())

# recoger los valores de un diccionario

print(mi_diccionario.values())

# recoger los pares clave/valor de un diccionario

print(mi_diccionario.items())