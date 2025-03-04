from openpyxl import load_workbook
from tabulate import tabulate

def exibir_planilha(planilha):
    tabela = [linha for linha in planilha.iter_rows(values_only=True)]
    print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

def edita_planilha(caminho_arquivo, nome_planilha, celula, novo_valor):
    try:
        # Carregar o arquivo Excel
        workbook = load_workbook(caminho_arquivo)
        
        # Selecionar a planilha desejada
        if nome_planilha in workbook.sheetnames:
            planilha = workbook[nome_planilha]
        else:
            print(f"A planilha '{nome_planilha}' não foi encontrada no arquivo.")
            return
        
        # Exibir a planilha antes da edição
        print("Planilha antes da edição:")
        exibir_planilha(planilha)
        
        # Editar a célula especificada
        planilha[celula] = novo_valor
        
        # Salvar as alterações no arquivo
        workbook.save(caminho_arquivo)
        print(f"Valor da célula {celula} atualizado para '{novo_valor}' na planilha '{nome_planilha}'.")
        
        # Exibir a planilha após a edição
        print("Planilha após a edição:")
        exibir_planilha(planilha)
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao editar a planilha: {e}")

if __name__ == "__main__":
    caminho_arquivo = input("Informe o caminho do arquivo Excel: ")
    nome_planilha = input("Informe o nome da planilha: ")
    celula = input("Informe a célula que deseja editar (por exemplo, A1): ")
    novo_valor = input("Informe o novo valor para a célula: ")
    
    edita_planilha(caminho_arquivo, nome_planilha, celula, novo_valor)