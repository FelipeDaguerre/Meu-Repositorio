# parâmetro que vai embalar todos os argumentos em uma dicionário, util para que a função possa aceitar uma variedade de argumentos-chave.

def saudações(**kwargs):
    print("Olá", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

saudações(titulo="senhor(a)", nome="Alan", sobrenome="Richard")