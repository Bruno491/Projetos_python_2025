import os
from vizualizar_planilha import vizualizar_planilha

PASTAS_PADRAO = [
    'C:\\Users\\bruno\\OneDrive\\Área de Trabalho',
    'C:\\Users\\bruno\\Downloads',
    'C:\\Users\\bruno\\OneDrive\\Documentos'
]

def obter_nome_arquivo():
    return input("Informe o nome do arquivo Excel: ")

def verificar_arquivo(pastas, nome_arquivo):
    for pasta in pastas:
        caminho_arquivo = os.path.join(pasta, f'{nome_arquivo}.xlsx')
        if os.path.isfile(caminho_arquivo):
            return caminho_arquivo
    return None

def criar_novo_arquivo():
    nome_novo_arquivo = input('Informe o nome para o novo arquivo: ')
    pasta_novo_arquivo = input('Informe a pasta para salvar o novo arquivo: ')
    caminho_novo_arquivo = os.path.join(pasta_novo_arquivo, f'{nome_novo_arquivo}.xlsx')
    # Aqui você pode adicionar a lógica para criar o arquivo de fato
    print(f'O arquivo {nome_novo_arquivo}.xlsx foi criado na pasta: {pasta_novo_arquivo}')

def procurar_planilha():
    nome_arquivo = obter_nome_arquivo()
    caminho_arquivo = verificar_arquivo(PASTAS_PADRAO, nome_arquivo)

    if caminho_arquivo:
        print(f'O arquivo {nome_arquivo}.xlsx foi encontrado na pasta: {os.path.dirname(caminho_arquivo)}')
        if input('Deseja visualizar a planilha? (S/N): ').strip().upper() == 'S':
            vizualizar_planilha()
    else:
        print(f'O arquivo {nome_arquivo}.xlsx não foi encontrado.')
        if input('Deseja criar um novo arquivo? (S/N): ').strip().upper() == 'S':
            criar_novo_arquivo()
        else:
            print('Nenhum novo arquivo foi criado.')

if __name__ == "__main__":
    procurar_planilha()