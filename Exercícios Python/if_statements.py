idade = int(input("Qual a sua idade? "))

if idade >= 100:
    print("O(a) senhor(a) ja é um(a) centenário(a)!")
elif idade <= 0:
    print("Você ainda não nasceu!")
elif 14 < idade <= 17:
    print("Você é um(a) adolescente!")
elif idade >= 61 <= 99:
    print("O(a) senhor(a) ja é idoso(a)!")
elif idade >= 18 <= 60:
    print("Você ja é adulto(a)!")
else:
    print("Você ainda é uma criança!")