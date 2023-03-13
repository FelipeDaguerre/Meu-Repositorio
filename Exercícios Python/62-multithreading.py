import threading
import time

# thread = um fluxo de execução. Como uma ordem separada de instruções. No entanto, cada thread leva um turno executando para atingir a simultaneidade

# GIL = (bloqueio do interpretador global) permite que apenas um thread mantenha o controle do interpretador Python a qualquer momento.

# vinculado ao CPU = programa/tarefa gasta a maior parte do tempo esperando por eventos internos (CPU intensivo), usa multiprocessamento

# vinculado ao input/ouput = o programa/tarefa passa a maior parte do tempo esperando por eventos externos (entrada do usuário, web scraping), usa multithreading

def comer_lanche():
    time.sleep(3)
    print("Você terminou de comer")

def tomar_café():
    time.sleep(4)
    print("Você terminou seu café da manhã")


def estudar():
    time.sleep(5)
    print("Você terminou seus estudos por hoje")

x = threading.Thread(target=comer_lanche, args=())
x.start()
y = threading.Thread(target=tomar_café, args=())
y.start()
z = threading.Thread(target=estudar, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
