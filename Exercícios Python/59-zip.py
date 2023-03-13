# zip(iteráveis) = agrega elementos de 2 ou mais iteráveis (listas, tuplas, conjuntos, ets.)           

login = ["Denis", "Diego", "Vinicius"]
senha = ("senha", "123456", "password")
datas_de_login = ["10/03/2023","11/03/2023","12/03/2023"]

usuarios = zip(login, senha, datas_de_login)

for i in usuarios:
    print(i)

