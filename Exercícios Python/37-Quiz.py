def novo_jogo(): 

    chutes = []
    chutes_corretos = 0
    num_questao = 1

    for key in perguntas:
        print("--------------------------")
        print(key)
        for i in opcs[num_questao-1]:
            print(i)
        chute = input("Digite (A, B, C, D ou E): ").upper()
        chutes.append(chute)

        chutes_corretos += conferir_pergunta(perguntas.get(key),chute)
        num_questao += 1

    display_score(chutes_corretos, chutes)
        
    
#--------------------------
def conferir_pergunta(resposta,chutes):
    
    if resposta == chutes:
        print("Acertou!")
        return 1
    else:
        print("Errou!")
        return 0
#--------------------------
def display_score(chutes_corretos, chutes):
    print("--------------------------")
    print("Resultado")
    print("--------------------------")

    print("As respostas foram: ",end=" ")
    for i in perguntas:
        print(perguntas.get(i),end=" ")
    print()

    print("As tentativas foram: ",end=" ")
    for i in chutes:
        print(i, end=" ")
    print()

    ponts = int((chutes_corretos/len(perguntas))*100)
    print("Você acertou: "+str(ponts)+"%"+" das perguntas")
#--------------------------
def jogar_denovo():
    escolha = input("Quer jogar denovo? (digite sim caso queira, ou digite qualquer coisa para encerrar): ").upper()

    if escolha == "SIM" or escolha == "S":
        return True
    else:
        return False
#--------------------------

perguntas = {
    "Quais as duas línguas mais faladas no mundo?\n":"B",
    "Quem inventou a lâmpada?\n":"C",
    "Quantos ossos temos no nosso corpo?\n":"B",
    "Onde se localiza Machu Picchu?\n":"B",
    "Quem foi a primeira pessoa a viajar no Espaço?\n":"A",
    "Qual a montanha mais alta do mundo?\n":"D"
}

opcs = [
["A) Inglês e espanhol","B) Inglês e mandarim chinês","C) Mandarim chinês e francês","D) Inglês e português","E) Inglês e espanhol"],
           
["A) Graham Bell","B) Steve Jobs","C) Thomas Edison","D) Henry Ford","E) Santos Dumont"],
        
["A) 126","B) 206","C) 18","D) 300","E) 200"], 

["A) Colômbia","B) Peru","C) China","D) Bolívia","E) Índia"],

["A) Yuri Gagarin","B) Alan Shepard","C) Neil Armstrong","D) Marcos Pontes","E) Buzz Aldrin"],

["A) Mauna Kea","B) Dhaulagiri","C) Monte Chimborazo","D) Monte Everest","E) Pico da Neblina"]
]

novo_jogo()

while jogar_denovo():
    novo_jogo()
    
print("Até a proxima!")