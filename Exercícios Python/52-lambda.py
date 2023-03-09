# lambda = função escrita utilizando a palavra-chave "lambda", aceita qualquer número de argumentos, mas apenas uma expressão. Pense nela como um "atalho".

dobro = lambda a: a * 2
print(dobro(50))

multiplicar = lambda a, b: a * b
print(multiplicar(2,8))

somar = lambda a, b, c: a + b + c
print(somar(5,6,3))

nome_completo = lambda primeiro_nome, sobre_nome: primeiro_nome+" "+sobre_nome
print(nome_completo("Felipe","Daguerre"))

conferir_maioridade = lambda idade:True if idade >= 18 else False

print(conferir_maioridade(17))