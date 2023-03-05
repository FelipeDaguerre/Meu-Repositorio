import random

while True:

    escolhas = ["pedra","papel","tesoura"]

    computador = random.choice(escolhas)
    jogador = None

    while jogador not in escolhas:
        jogador = input("Escolha: pedra, papel ou tesoura? ").lower()

    if jogador == computador:
        print("\nO jogador escolheu:",jogador)
        print("O computador escolheu:",computador)

        print("\nEmpate!")

    elif jogador == "pedra":
        if computador == "tesoura":
            print("\nO jogador escolheu:",jogador)
            print("O computador escolheu:",computador)
            print("\nVocê ganhou, Parabéns!")
        if computador == "papel":
            print("\nO jogador escolheu:",jogador)
            print("O computador escolheu:",computador)
            print("\nVocê perdeu, que pena!")

    elif jogador == "tesoura":
        if computador == "papel":
            print("\nO jogador escolheu:",jogador)
            print("O computador escolheu:",computador)
            print("\nVocê ganhou, Parabéns!")
        if computador == "pedra":
            print("\nO jogador escolheu:",jogador)
            print("O computador escolheu:",computador)
            print("\nVocê perdeu, que pena!")

    elif jogador == "papel":
        if computador == "pedra":
            print("\nO jogador escolheu:",jogador)
            print("O computador escolheu:",computador)
            print("\nVocê ganhou, Parabéns!")
        if computador == "tesoura":
            print("\nO jogador escolheu:",jogador)
            print("O computador escolheu:",computador)
            print("\nVocê perdeu, que pena!")
             
    repetir = input('Quer jogar denovo? ( s - sim/ n - não): ').lower()

    if repetir != "s":
        break

print("\nAté a próxima!")
