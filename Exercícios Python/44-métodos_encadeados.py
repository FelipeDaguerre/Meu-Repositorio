# métodos encadeados = chama multiplos métodos em sequencia, cada chamada irá realizar uma ação no mesmo objeto e retornar "self"

class Carro():
    def ligar(self):
        print("Você ligou o carro")
        return self
    
    def dirigir(self):
        print("Você está dirigindo")
        return self
    
    def frear(self):
        print("Você pisou no freio")
        return self
    
    def desligar(self):
        print("Você desligou o carro")
        return self
    
carro = Carro()

carro.ligar()\
     .dirigir()\
     .frear()\
     .desligar()