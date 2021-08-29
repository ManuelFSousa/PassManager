from login import check_pass, new_pass
import cripto
import login 
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') #Comandos para limpar a consola nos diferentes sistemas operativos

def login():
    clearConsole()
    print(""" 
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' 
    """)
    print("         Gestor de Palavras Passes V1\n")

    user = input("Utilizador: ")
    password = input("Password: ")

    return check_pass(user, password), user

def imprimirMenu1():
    print(""" 
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' 
    """)
    print("         Gestor de Palavras Passes V1\n")
    print("\nEscolha o que deseja fazer:")
    print("1 - Fazer Login")
    print("2 - Criar Novo Login")
    print("3 - Fechar Programa")


def imprimirMenu2():
    clearConsole()
    print(""" 
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' 
    """)
    print("         Gestor de Palavras Passes V1\n")
    print("\nEscolha o que deseja fazer:")
    print("1 - Guardar Nova Palavra Passe")
    print("2 - Pedir Palavra Passe")
    print("3 - Mudar utilizador")
    print("4 - Fechar Programa")


def loginEfetuado(user):
    escolha = 1
    key = cripto.check_key(user)

    while escolha > 0 or escolha < 6:
        imprimirMenu2()
        escolha = int(input("\nA sua opção: "))
        if escolha == 1:
            clearConsole()
            print("Qual o nome do programa do qual quer guardar a password?")
            programa = input()
            cripto.save_pass(user, programa.lower(), key)

        elif escolha == 2:
            clearConsole()
            print("Qual o nome do programa do qual quer ver a password?")
            programa = input()
            cripto.load_pass(user, programa.lower(), key)

        elif escolha == 3:
            return 3

        elif escolha == 4:
            return 4


def main():
    while 1:
        clearConsole()
        imprimirMenu1()
        escolha = int(input("\nA sua opção: "))
        if escolha == 1:
            valor, user = login()
            if valor == 1:
                next = loginEfetuado(user)
                if next == 4:
                    clearConsole()
                    return 0

            elif login != 1 and next != 3:
                print("Erro no Login!")
                return 0
        elif escolha == 2:
            new_pass()
        elif escolha == 3:
            clearConsole()
            return 0
        else:
            print("A opção escolhida não é válida")
        




if __name__ == "__main__":  #Quando abro diretamente este ficheiro, a variável especial "__name__" tem a string "__main__"
    main()                  #atribuída. Isto acontece por definição. Caso este módulo seja chamado por outro programa,
                            #a variável "__name__" fica com a string igual ao nome (neste caso seria só "main").

#here: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
#https://devqa.io/encrypt-decrypt-data-python/
