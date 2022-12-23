
class Animal:

    def __init__(self,patas,alimento,tipo):
        self.patas = patas
        self.alimento = alimento
        self.tipo = tipo
    
    def comer(self):
        print(f"estoy comiendo {self.alimento}")

    def caminar(self):
        print(f"estoy caminando sobre {self.patas} pata(s)")

if __name__ == '__main__':
    
    class Gato(Animal):
        def __init__(self):
            Animal.__init__(self,4,'pescado','animal doméstico')
        
        def maullar(self):
            print('miau miau miau')
    miGato = Gato()
    miGato.caminar()
