# herança multinível = quando a classe filha herda a classe de outra filha, nesse caso o organismo ficou sendo o "avô" da classe "cachorro"

class Organismo:
    vivo = True

class Animal(Organismo):
    def comer(self):
        print("Este animal está comendo")

class Cachorro(Animal):
    def latir(self):
        print("Este cachorro está latindo")


cachorro = Cachorro()

print(cachorro.vivo)
cachorro.comer()
cachorro.latir()
    