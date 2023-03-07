# impede o usuário de criar um objeto dessa classe
# + obriga o usar a substituir o método abstrato em uma classe filha

# classe abstrata = uma classe um ou mais métodos abstratos.
# método abstrato = um método que foi declarado mas não pode ser implementado.


from abc import ABC, abstractclassmethod

class Veículo(ABC):

    @abstractclassmethod
    def partida(self): 
        print("Este veículo deu partida")

    @abstractclassmethod
    def parar(self):
        pass

class Carro(Veículo):
    def partida(self):
        print("Este carro deu partida")

    def parar(self):
        print("Este carro parou")

class Motocicleta(Veículo):
    def partida(self):
        print("Essa motocicleta deu partida")
    
    def parar(self):
        print("Essa motocicleta parou")

carro = Carro()
moto = Motocicleta()

# veículo = Veículo()
# veículo.partida

carro.partida()
moto.partida()
carro.parar()
moto.parar()
