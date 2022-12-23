# Para manejar posibles errores en Python usamos try,except y finally
# Dentro de try escribiremos el código que queremos que se ejecuter
# Dentro de except escribiremos el código que se ejecutará en caso de error
# Dentro de finally escribiremos el código que queremos que se ejecute en cualquier caso, haya error o no

try:
    print(10 + '10')
except:
    print('Vaya... parece que ha surgido un error, revisa que no hayas tenido algún despiste manipulando el código')
finally:
    print('El código ha sido ejecutado')