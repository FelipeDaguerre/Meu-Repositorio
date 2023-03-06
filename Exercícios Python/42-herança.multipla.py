# herança multipla = quando uma classe filha é derivada de mais de uma classe parente, nesse caso a classe "Peixe"

class Presa:
    
    def fugir(self):
        print("Este animal está fogindo")

class Predador:
    
    def caçar (self):
        print("Este animal está caçando")

class Coelho(Presa):
    pass

class Peixe(Presa, Predador):
    pass

class Falcão(Predador):
    pass

coelho = Coelho()
peixe = Peixe()
falcao = Falcão()

coelho.fugir()
peixe.fugir()
peixe.caçar()
falcao.caçar()