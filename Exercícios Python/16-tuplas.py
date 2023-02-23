# tupla = uma coleção que ordenada e inalterável, usada para agrupar dados que tem ligação


estudante = ("Aline", 26, "feminino")

print(estudante.count("Aline"))
print(estudante.index("feminino"))

for i in estudante:
    print(i)

if "Aline" in estudante:
    print("Aline está aqui!")