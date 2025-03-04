def exibir_menu():
    print('Lista de contatos do centro de impressão')
    print('1- Usuario1')
    print('2- Usuario2')
    print('Selecione um usuário para enviar o e-mail ou tecle "0" para voltar')

def obter_opcao():
    try:
        return int(input('Opção: '))
    except ValueError:
        print('Entrada inválida, por favor insira um número.')
        return None

def lista_3():
    while True:
        exibir_menu()
        op_cont = obter_opcao()
        
        if op_cont is None:
            continue
        
        if op_cont == 1:
            return 'Usuario1@outlook.com'
        elif op_cont == 2:
            return 'Usuario2@outlook.com'
        elif op_cont == 0:
            print('Voltando...')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    email = lista_3()
    if email:
        print(f'Email selecionado: {email}')