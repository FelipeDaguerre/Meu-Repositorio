
# sort() method   = utilizado com listas
# sort() function = usado com iteráveis

# estudantes_1 = ("Nate", "Danila", "Ludmilla", "Juliano", "Ramon")

# organizados = sorted(estudantes_1)

# for i in organizados:
#     print(i)


estudantes = (("Cassio", "8", 45),
            ("Alicia", "9", 29),
            ("Carla","8", 23),
            ("Richard","7.5", 24),
            ("Lucio","6", 30))

idade = lambda idade:idade[2]                 
estudantes_organizados = sorted(estudantes,key=idade) 

for i in estudantes_organizados:
    print(i)