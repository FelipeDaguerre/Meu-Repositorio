
# Python multiprocessamento

# multiprocessamento = executando tarefas em paralelo em diferentes núcleos de CPU, ignora o GIL usado para threading.

# multiprocessamento = melhor para tarefas ligadas à CPU (uso intenso da CPU)
# multithreading = melhor para tarefas vinculadas y io (esperando input do usuário)

import time
from multiprocessing import Process, cpu_count

def contador(num):
    contagem = 0
    while contagem < num:
        contagem += 1


def main():

    print("numero de núcleos do meu PC:", cpu_count()) # No meu caso, tenho 8

    a = Process(target=contador, args=(125000000,))
    b = Process(target=contador, args=(125000000,))
    c = Process(target=contador, args=(125000000,))
    d = Process(target=contador, args=(125000000,))
    e = Process(target=contador, args=(125000000,))
    f = Process(target=contador, args=(125000000,))
    g = Process(target=contador, args=(125000000,))
    h = Process(target=contador, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    print("aguarde...")

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print("Acabou!")
    s = time.perf_counter()
    print("Completado em:", time.perf_counter()-s, "segundos")

if __name__ == "__main__":
    main()
    
