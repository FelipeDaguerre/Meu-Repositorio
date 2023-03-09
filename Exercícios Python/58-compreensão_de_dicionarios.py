
# compreensão de dicionarios = cria dicionarios usando uma expressão, pode substituir for loops e certas funções lambda

cidades_em_fahrenheit = {'Aracaju':79.88, 'Belo Horizonte': 70.16, 'Macapa': 74.48, 'Porto Alegre': 73.4,'Rio de Janeiro': 72.86, 'Teresina': 77}

cidades_em_celcius = {chave: round((valor-32)*(5/9)) for (chave,valor) in cidades_em_fahrenheit.items()}

print(cidades_em_celcius)


def checar_temperatura(valor):
    if valor <= 25:
        return "Está morno"
    elif valor == 26:
        return "Está quente la fora"
    
clima_cidades = {chave:checar_temperatura(valor) for (chave,valor) in cidades_em_celcius.items()}

print(clima_cidades)

