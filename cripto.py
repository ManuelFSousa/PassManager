import os.path
from os import path
from cryptography.fernet import Fernet

def check_key(user):
    if path.exists(os.getcwd() + "/sys/" + user + "/" + user + "-key.key") == False:
        key = Fernet.generate_key()
        with open(os.getcwd() + "/sys/" + user + "/" + user + "-key.key" , "wb") as key_file:
            key_file.write(key)
            key_file.close()
            return key
    else:
        return open(os.getcwd() + "/sys/" + user + "/" + user + "-key.key","rb").read()

def save_pass(user, website, key):
    f = Fernet(key)

    if path.exists(os.getcwd() + "/sys/" + user + "/" + website + "-key.key"):
        print("Palavra Passe já guardada. Deseja substituir? (y/n)")
        opcao = input()
        if(opcao == "n"):
            return 1

    with open(os.getcwd() + "/sys/" + user + "/" + website + "-key.key", "wb") as ficheiro:
        print("Qual é o username?")
        username = input()
        print("Qual é a pass?")
        passwd = input()

        encriptar = "\nUsername: " + username + "\n" + "Password: " + passwd + "\n"
        ficheiro.write(f.encrypt(encriptar.encode()))
        ficheiro.close()
        print("Password Guardada com Sucesso")
        return 1

def load_pass(user, website, key):
    if path.exists(os.getcwd() + "/sys/" + user + "/" + website + "-key.key") == False:
        print("Palavra Passe não existente")
        return 0

    f = Fernet(key)

    ficheiro = open(os.getcwd() + "/sys/" + user + "/" + website + "-key.key","rb")
    imprimir = f.decrypt(ficheiro.read())
    print(imprimir.decode())
    ficheiro.close()

    print("Prima qualquer tecla para avançar.")
    input()
    return 1