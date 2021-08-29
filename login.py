from passlib.hash import sha256_crypt
from os import path
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') #Comandos para limpar a consola nos diferentes sistemas operativos

def new_pass():
    clearConsole()
    print("Criação de um Novo Utilizador\n")

    if path.exists(os.getcwd() + "/sys/") == False:
        os.mkdir(os.getcwd() + '/sys')

    print("Qual é o novo utilizador? (Para cancelar deixe em branco)")
    user = input()
    if user == '':
        return 0
    if path.exists(os.getcwd() + "/sys/" + user + "/" + user + ".key") == True:
        print("O utilizador já existe.")
        return 0

    os.mkdir(os.getcwd() + '/sys/' + user)
    print("Qual é a nova password para o login?")
    passe = input()
    print("Repita a password, por favor.")
    passe2 = input()
    
    if passe == passe2:
        f = open(os.getcwd() + "/sys/" + user + "/" + user + ".key" , "w")
        password = sha256_crypt.encrypt(passe + "hJwOcmG")
        f.write(password)
        f.close()
        print("Login Criado Com Sucesso!")
        return 1

    print("As Passwords não são correspondentes")
    return 0



def check_pass(user, password):
    if path.exists(os.getcwd() + "/sys/" + user + "/" + user + ".key") == True:
        f = open(os.getcwd() + "/sys/" + user + "/" + user + ".key", "r")
        hashed = f.read()
        f.close()
    else:
        print("O utilizador está errado.")
        return 0

    if sha256_crypt.verify(password + "hJwOcmG", hashed) == True:
        print("Login efetuado com sucesso!")
        return 1
    else:
        print("A password está errada.")
        return 0