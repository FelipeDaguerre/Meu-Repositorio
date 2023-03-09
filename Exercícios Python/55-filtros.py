# filter() = cria uma coleção de elementos de um iterável, para o qual uma função retorna apenas quem for verdadeiro. filtro(função, iterável)

parceiros = [("Raquel",17),
           ("Aline",23),
           ("José",17),
           ("Valmir",25),
           ("Rafael",19),
           ("Douglas",16)]

idade = lambda data:data[1] >= 18

parceiros_de_bebida = list(filter(idade, parceiros))

for i in parceiros_de_bebida:
    print(i)