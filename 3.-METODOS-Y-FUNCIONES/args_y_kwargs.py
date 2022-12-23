# *args
# Nos permite usar un número indefinido de parámetros 

def sum_num(*args):
    return sum(args)


print(sum_num(1,2,3,4,5,6,7,8,9,10))


# *kwargs
# Nos permite tener parámetros nombrados en nuestras funciones

def get_stock(**kwargs):
    return f"Hoy en la tienda tenemos {kwargs['cereales']}"

print(get_stock(cereales='corn flakes',fruta='sandía',sopa='avecrem de pollo'))

# USO COMBINADO DE *ARGS Y *KWARGS


def rewards(*premios,**ganadores):
    
    return f"{ganadores['Rafael_Nadal']} ha ganado {premios[0]} trofeos en su carrera"

print(rewards(90,19,Usain_Bolt = 'el mejor corredor de la historia',Rafael_Nadal='el mejor tenista de todos los tiempos'))