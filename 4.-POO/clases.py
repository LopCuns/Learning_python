class Perro():
    def __init__(self,raza,nombre,caracter):
        self.raza = raza
        self.nombre = nombre
        self.caracter = caracter
    
    def ladrar(self):
        print('Guuuaaauuuu guaauuuu guuuuuaaaaauuuuuu')


chipi = Perro('yorkshire terrier','Chipi','agresivo/defensivo') #los parámetros se pueden pasar por orden
gruñon = Perro(raza = 'yorkshire terrier',nombre = 'Gruñon',caracter = 'tranquilo') #los parámetros se pueden pasar por nombre

chipi.ladrar()
gruñon.ladrar()



# HERENCIA Y POLIMORFISMO
# A partir de la clase Animal, vamos a crear la clase gato y cabra (dos polimorfos de animal) que van a heredar sus atributos y funciones
class Animal:

    def __init__(self,patas,alimento,tipo):
        self.patas = patas
        self.alimento = alimento
        self.tipo = tipo
    
    def comer(self):
        print(f"estoy comiendo {self.alimento}")

    def caminar(self):
        print(f"estoy caminando sobre {self.patas} pata(s)")


class Gato(Animal):
    def __init__(self):
        Animal.__init__(self,4,'pescado','animal doméstico')
    
    def maullar(self):
        print('miau miau miau')


class Cabra(Animal):
    def __init__(self):
        Animal.__init__(self,alimento = 'pasto',tipo = 'animal montés', patas = 4)
    
    def envestir(self):
        print('st st st fuuuuuuun')

miGato = Gato()
miGato.caminar()

miCabra = Cabra()
miCabra.envestir()