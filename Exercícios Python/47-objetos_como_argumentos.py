class Carro:
    cor = None

def mudar_cor(carro,cor):

    carro.cor = cor

class Motocicleta:
    cor = None

carro_1 = Carro()
carro_2 = Carro()
carro_3 = Carro()
moto_4 = Motocicleta()

mudar_cor(carro_1,"vermelho")
mudar_cor(carro_2,"verde")
mudar_cor(carro_3,"azul")
mudar_cor(moto_4,"cinza")

print(carro_1.cor)
print(carro_2.cor)
print(carro_3.cor)
print(moto_4.cor)