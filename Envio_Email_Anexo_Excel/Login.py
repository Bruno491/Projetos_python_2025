import sys
import os
from Menu import Menu

USUARIO_PATH = "C:\\Users\\bruno\\OneDrive\\Documentos\\usuario.txt"

def obter_credenciais():
    email = input("Email: ")
    password = input("Senha: ")
    return email, password

def verificar_credenciais(email, password):
    if os.path.exists(USUARIO_PATH):
        with open(USUARIO_PATH, "r") as f:
            users = f.read().splitlines()
        for user in users:
            user_email, user_password = user.split(":")
            if user_email == email and user_password == password:
                return True
    return False

def criar_conta(email, password):
    with open(USUARIO_PATH, "a") as f:
        f.write(f"{email}:{password}\n")
    print("Conta registrada com sucesso!")

def main():
    email, password = obter_credenciais()
    
    if verificar_credenciais(email, password):
        print("Bem vindo!")
        Menu()
    else:
        print("Email e/ou senha inválido!")
        if not os.path.exists(USUARIO_PATH):
            print("Usuário não encontrado! Por favor, crie uma conta.")
            if input("Deseja criar uma conta? (S/N): ").strip().upper() == "S":
                criar_conta(email, password)

if __name__ == "__main__":
    main()