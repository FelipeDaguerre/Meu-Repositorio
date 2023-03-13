import time

# print(time.ctime(0)) # converte um valor em segundos desde o "epoch" para uma string.
                       # epoch = o momento que seu computador acha que o tempo começou, serve para um ponto de referencia.


# print(time.time())      # retorna quantos segundos se passaram desde o epoch
# print(time.ctime(time.time())) # mostra o horario atual


tempo_obj = time.localtime() # horario local
tempo_obj = time.gmtime() # horario UTC = "universal time coordinated" ou "hora mundial coordenada"

hora_local = time.strftime("%d %B %Y %H:%M:%S", tempo_obj) # mostra a data e horario atual
print(hora_local)


