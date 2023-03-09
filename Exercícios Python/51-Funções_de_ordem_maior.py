# função de ordem maior = uma função que: aceita uma função como argumento ou retorna uma função. Em python, as funções também são tratadas como objetos.

def gritar(texto):
    return texto.upper()

def sussurrar(texto):
    return texto.lower()

def ola(funcao):
    texto = funcao("Tem alguém ai?")
    print(texto)

ola(gritar)
ola(sussurrar)

# retornando uma função
#def divisor(x):
   #def dividendo(y):
       #return y / x
   #return dividendo


#dividir = divisor(3)
#print(dividir(10))