#dicionario = uma coleção única, não-ordenada de valores-chave pares únicos.

capitais = {"Brasil": "Brasília", 
            "Índia":"Nova Delhi", 
            "Argentina":"Buenos Aires",
            "China":"Beijing",
            "Russia":"Moscow"}

#capitais.update({"Brasil":"Salvador"})
#capitais.pop("Russia")
#capitais.clear()

#print(capitais["Índia"])
#print(capitais.keys())
#print(capitais.values())
#print(capitais.items())
#print(capitais.get("Alemanha"))

for key,value in capitais.items():
    print(key, value)