# super() = função usada para dar acesso ao método de uma classe parente. Retorna um objeto temporario de uma classe parente quando usado

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura


class Quadrado(Retangulo):
    def __init__(self, comprimento, largura):
        super().__init__(comprimento,largura)

    def area(self):
        return self.comprimento*self.largura

class Cubo(Retangulo):
    
    def __init__(self, comprimento, largura, altura):
        super().__init__(comprimento,largura)
        self.altura = altura

    def volume(self):
        return self.comprimento*self.largura*self.altura

quadrado = Quadrado(3, 3)
cubo = Cubo(3, 3, 3)

print(quadrado.area())
print(cubo.volume())

