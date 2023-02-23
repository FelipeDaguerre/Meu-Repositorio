#operadores logicos (and, or) = usados para verificar uma ou mais condições.

temperatura = int(input("Qual a temperatura em graus celsius la fora? "))

#if temperatura >= 5 and temperatura <= 40:
 #   print("A temperatura está boa! ")
 #   print("Vá lá fora!")
#elif temperatura <= 4 or temperatura >= 41:
 #   print("a temperatura está ruim!")
 #   print("Fique dentro de casa!")


# operador (not) altera o valor de verdadeiro para falso ou vice-versa.

if not(temperatura >= 5 and temperatura <= 40):
    print("a temperatura está ruim!")
    print("Fique dentro de casa!")
    
elif not (temperatura <= 4) or (temperatura >= 41):
    print("A temperatura está boa! ")
    print("Vá lá fora!")



