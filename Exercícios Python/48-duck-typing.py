# duck typing (tipagem pato) = o conceito onde a classe de um objeto é menos importante que seus métodos ou atributos, o tipo de classe não é checado se os atributos / métodos mínimos estiverem presente.

# é baseado em uma frase popular "Se anda como pato, fala como pato, nada como pato e tem cara de pato, então é pato"


class Cachorro:

    def falar(self):
        print("Este cachorro está latindo")

    def andar(self):
        print("Este cachorro está andando")

class Gato:

    def falar(self):
        print("Este gato está miando")

    def andar(self):
        print("Este gato está andando")

class Pessoa:

    def capturar(self, cachorro):
        cachorro.falar()
        cachorro.andar()
        print("Você capturou ele!")


gato = Gato()
cachorro = Cachorro()
pessoa = Pessoa()

pessoa.capturar(gato)