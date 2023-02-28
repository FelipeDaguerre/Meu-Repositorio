# str.format() = método opcional que da ao usuário mais controle ao mostrar os resultados.

numero = 1000

print("O número pi é de {:.3f}".format(numero))
print("O número é {:,}".format(numero))
print("O número é {:b}".format(numero))
print("O número é {:0}".format(numero))
print("O número é {:X}".format(numero))
print("O número é {:E}".format(numero))

animal = "vaca"
item = "lua"
print("A {} saltou sobre a {}".format(animal,item))