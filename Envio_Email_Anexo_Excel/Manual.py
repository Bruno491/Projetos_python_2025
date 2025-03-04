import os

def manual():
    opm = int('0')
    while opm != 4:
        print('Sobre o que você quer ver?')
        print('1- Procurar pela planilha no dispositivo')
        print('2- Enviar relatório por e-mail')
        print('3- Prosso utilizar esse programa em outro equipamento?')
        print('4- Voltar')
        opm = int(input('Opção: '))
        os.system('cls')
        if opm == 1:
            print('Para procurar o arquivo, será necessario apenas o nome referente ao mesmo.')
            os.system('pause')
            os.system('cls')
            print('A opção de procurar por planilha serve para procurar arquivos dentro das seguintes pastas:\n')
            print('Area de trabalho\n')
            print('Downloads\n')
            print('Documentos')
            os.system('pause')
            os.system('cls')
        elif opm == 2:
            print('A opção de enviar arquivo por e-mail, seve para enviar email com o arquivo que voce quiser anexar sem precisar de um navegador')
            os.system('pause')
            os.system('cls')
            print('Para enviar o e-mail junto ao arquivo você ira precisar das seguintes informações:\n')
            print('O email do remetente;\n')
            print('A senha referente ao email do remetente;\n')
            print('O email do destinatario;\n')
            print('E arquivo que deseja enviar;')
            os.system('pause')
            os.system('cls')
        elif opm == 3:
            print('Não, esse programa foi feito para ser utilizado APENAS neste equipamento\n')
            print('Caso seja detectado a tentativa de utilização do mesmo em outro equipamento\n')
            print('A equipe de desenvolvimento será alertada')
            os.system('pause')
            os.system('cls')