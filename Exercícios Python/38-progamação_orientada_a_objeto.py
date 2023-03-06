from carro import Carro

carro_1 = Carro("Ford","Sedan","2020","azul")
carro_2 = Carro("Honda","Civic","2019","cinza")

print(carro_1.marca)
print(carro_2.modelo)
print(carro_1.ano)
print(carro_2.cor)

carro_1.dirigir()
carro_1.parar()