# loop aninhado = um loop dentro de outro loop. O "loop interno" irá terminar todas as suas iterações antes de realizar interações do "loop externo".


linhas = int(input("Quantas linhas deseja? "))
colunas = int(input("Quantas colunas deseja? "))
simbolo = input("Digite um simbolo: ")

for i in range(linhas):
    for j in range(colunas):
        print(simbolo, end="")
    print()