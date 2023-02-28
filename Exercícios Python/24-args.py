# parâmetro que vai embalar todos os argumentos em uma tupla, util para que a função possa aceitar uma variedade de argumentos.

def add(*args):         
    soma = 0
    #args = list(args)
    #args[0] = 0
    for i in args:
        soma += i
    return soma
    
print(add(1,2,3,4,5,6,7))   