
linhas = int(input("Quantas linhas deseja? "))
colunas = int(input("Quantas colunas deseja? "))
simbolo = input("Digite um simbolo: ")

for i in range(linhas):
    for j in range(colunas):
        print(simbolo, end="")
    print()