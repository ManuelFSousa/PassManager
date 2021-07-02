import cripto.py

def login():
    print(""" 
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' 
    """)
    print("Gestor de Palavras Passes V1")

    user = input("Utilizador: ")
    password = input("Password: ")

    FILE


def imprimirMenu():
    print("\nEscolha o que deseja fazer:")
    print("1 - Guardar Nova Palavra Passe")
    print("2 - Pedir Palavra Passe")
    print("3 - Mudar utilizador")
    print("4 - Fechar Programa")

def savePass():
    print("algo")


def main():
    if login() == 1:
        print("Login bem sucedido!")
    else:
        print("Login inexistente!")
        return

    escolha = 1
    while escolha > 0 or escolha < 6:
        imprimirMenu()
        escolha = int(input("\nA sua opção: "))
        if escolha == 1:
            savePass()
        elif escolha == 5:
            break




if __name__ == "__main__":  #Quando abro diretamente este ficheiro, a variável especial "__name__" tem a string "__main__"
    main()                  #atribuída. Isto acontece por definição. Caso este módulo seja chamado por outro programa,
                            #a variável "__name__" fica com a string igual ao nome (neste caso seria só "main").

#here: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python