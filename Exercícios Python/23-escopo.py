# escopo = a região onde a variável é reconhecida, a variável só está disponível dentro da região onde foi criada, pode ser criada uma versão local ou global de uma variável.

nome = "Jonathan" # escopo global, disponível dentro e fora de funções.


def mostrar_nome():
    nome = "Alisson" # escopo local, disponível apenas dentro desta função.
    print(nome)

mostrar_nome()
print(nome)
