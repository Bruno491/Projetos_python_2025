import os
import socket
import time
from procurar_planilha import procurar_planilha
from Enviar_email import Enviar_email
from Manual import manual
from alerta import alerta
from edita_planilha import edita_planilha

VALIDAR_IP = '000.000.000.0'
HOST = 'google.com'
PORT = 80
MAX_TENTATIVAS = 3

def verificar_conexao():
    tentativa = 0
    while tentativa <= MAX_TENTATIVAS:
        try:
            with socket.create_connection((HOST, PORT), timeout=5) as s:
                print('Conexão estabelecida!')
                time.sleep(0.7)
                os.system('cls')
                return True
        except socket.error:
            print('Problema com a conexão, tentando novamente...')
            tentativa += 1
            time.sleep(1.2)
    return False

def obter_ip_rede():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]

def exibir_menu():
    while True:
        print('<<<<Menu>>>>')
        print('1- Procurar pela planilha no dispositivo')
        print('2- Enviar relatório por e-mail')
        print('3- Manual')
        print('4- Editar planilha')
        print('5- Sair')
        try:
            op = int(input('Opção: '))
            os.system('cls')
            if op == 1:
                procurar_planilha()
            elif op == 2:
                Enviar_email()
            elif op == 3:
                manual()
            elif op == 4:
                edita_planilha()
                break
            elif op == 5:
                print('Saindo...')
                time.sleep(2.1)
                os.system('cls')
            else:
                print('Opção inválida, tente novamente.')
        except ValueError:
            print('Entrada inválida, por favor insira um número.')

def Menu():
    if verificar_conexao():
        network_ip_address = obter_ip_rede()
        if network_ip_address != VALIDAR_IP:
            exibir_menu()
        else:
            alerta()
    else:
        print('Sem conexão com a internet')

if __name__ == "__main__":
    Menu()