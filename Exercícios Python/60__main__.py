# O módulo pode ser executado como um programa autônomo.
# O módulo pode ser importado e usado por outros módulos.

# O interpretador python define "variáveis ​​especiais", uma das quais é "__name__" python atribuirá à variável __name__ um valor de '__main__' se for o módulo inicial sendo executado.

def main():
    print("Olá")


if __name__ == "__main__":
    main()

    