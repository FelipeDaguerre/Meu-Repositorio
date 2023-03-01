try:
    with open('C:\\Users\\felip\\Desktop\\teste.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("O arquivo não foi encontrado:")