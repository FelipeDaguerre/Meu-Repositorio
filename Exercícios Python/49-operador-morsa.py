# operador morsa :=
# uma expressão de atribuir valores conhecida como "operador morsa"
# atribui valores a variáveis ​​como parte de uma expressão maior

# pratos = list()
# while True:
#   comida = input("De qual refeição você gosta?: ")
#       if comida == "sair":
#           break
#   pratos.append(comida)

pratos = list()
while (comida := input("De qual refeição você gosta?: ")) != "sair":
    pratos.append(comida)