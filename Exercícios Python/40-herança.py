# herança = quando a classe filha herda os atributos da classe pai (animal) nesse caso

class Animal:

    vivo = True

    def comer(self):
        print("Este animal está comendo")

    def dormir(self):
        print("Este animal está dormindo")

class Coelho(Animal):
    def correr(self):
        print("Este coelho está correndo")

class Falcão(Animal):
    def voar(self):
        print("Este falcão está voando")

class Peixe(Animal):
    def nadar(self):
        print("Este peixe está nadando")

coelho = Coelho()
peixe = Peixe()
falcao = Falcão()

# print(coelho.vivo)
# peixe.comer()
# falcao.dormir()

coelho.correr()
peixe.nadar()
falcao.voar()
