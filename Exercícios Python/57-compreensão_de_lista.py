# compreensão de lista = uma maneira de criar uma nova lista com menos linhas de código, pode imitar certas funções lambda e sendo mais fáceis de ler.

# lista = [expressão para item em iterável].
# lista = [expressão para item em iterável se condicional];
# lista = [expressão if/else para item em iterável].

# potencia = []
# for i in range (1,11):
#     potencia.append(i*i)
#     print(potencia)

# potencia = [i * i for i in range (1,11)]
# print(potencia)

estudantes = [100,90,80,70,60,50,40,30,0]

# estudantes_aprovados = list(filter(lambda x: x >= 60, estudantes))
# estudantes_aprovados = [i for i in estudantes if i >= 60]
estudantes_aprovados = [i if i >= 60 else "Reprovado" for i in estudantes]

print(estudantes_aprovados)