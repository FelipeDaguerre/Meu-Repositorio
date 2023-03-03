import os

fonte = "Teste.txt"
destino = "C:\\Users\\felip\\Desktop\\Teste.txt"

try:
    if os.path.exists(destino):
        print("Ja existe um arquilo ali")
    else:
        os.replace(fonte,destino)
        print(fonte+"Foi movido com sucesso")
except FileNotFoundError:
    print(fonte+"Arquivo não foi encontrado")