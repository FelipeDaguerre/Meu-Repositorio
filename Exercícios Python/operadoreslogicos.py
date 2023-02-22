temperatura = int(input("Qual a temperatura em graus celsius la fora? "))

if temperatura >= 5 and temperatura <= 40:
    print("A temperatura está boa! ")
    print("Vá lá fora!")
elif temperatura <= 4 or temperatura >= 41:
    print("a temperatura está ruim!")
    print("Fique dentro de casa!")

