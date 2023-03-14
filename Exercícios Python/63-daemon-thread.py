# daemon thread = uma thread que roda em segundo plano, não é importante para a execução do programa, seu programa não esperará que esses threads sejam concluídos antes de serem encerrados, ao contrário dos threads normais que ficarão ativos até que a tarefa seja concluída. 

# podem ser usados para tarefas em segundo plano, coleta de lixo, aguardando entrada do usuário ou processos de execução longa.

import threading
import time


def timer():
    print()
    contagem = 0
    while True:
        time.sleep(1)
        contagem += 1
        print("contando: ", contagem, "segundos")


x = threading.Thread(target=timer, daemon=True) #basta adicionar "daemon=True"
x.start()

# x.setDaemon(True)
# print(x.isDaemon())

resposta = input("Você deseja sair? \n")

