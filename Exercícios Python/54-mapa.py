# map() = aplica uma função para cada item em um iterável (lista, tuple, etc.)
# mapa (função,iterável)

loja = [("camisa",20.00),
         ("calça",25.00),
         ("jaqueta",50.00),
         ("meias",10.00)]

euro_real = lambda dados: (dados[0],dados[1]*5.41) # pagando em reais pra euro
dolar_real = lambda dados: (dados[0],dados[1]*5.13) # pagando em reais pra dolar

real_dolar = lambda dados: (dados[0],dados[1]/5.13) # pagando em dolar pra reais
real_euro = lambda dados: (dados[0],dados[1]/5.41) # pagando em euro pra reais

loja_euro = list(map(euro_real, loja))

for i in loja_euro:
    print(i)