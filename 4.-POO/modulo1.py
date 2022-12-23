from modulo2 import Animal  #así podemos importar clases de otros archivos python

class Raton(Animal):
    def __init__(self):
        Animal.__init__(self,4,'queso','animal de alcantarilla')

    def roer(self):
        print('chiu chiu')

miRaton = Raton()
miRaton.roer()
miRaton.comer()
