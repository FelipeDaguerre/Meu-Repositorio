def deposit():
    while True:
        quantidade = input ("Quanto deseja depositar? R$")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if quantidade > 0:
                break   
            else:
                print("A quantidade deve ser maior que 0.")
        else:
            print("Por favor use apenas números.")
    return quantidade