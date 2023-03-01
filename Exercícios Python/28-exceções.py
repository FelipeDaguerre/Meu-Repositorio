# exceções = eventos detectados durante a execução que interrompem o fluxo normal do programa

try: 
    numerador = int(input("Digite um número para dividir: "))
    denominador = int(input("Digite um número para ser dividido "))
    resultado = numerador / denominador

except ZeroDivisionError as e:
    print(e)
    print("Você não pode dividir por 0.")

except ValueError as e:
    print(e)
    print("Digite apenas números.")

except Exception as e:
    print(e)
    print("Algo deu errado")
else:
    print(resultado)
