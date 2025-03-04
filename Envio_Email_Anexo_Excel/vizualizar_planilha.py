from tabulate import tabulate
import openpyxl

def carregar_planilha(caminho_arquivo, nome_planilha):
    try:
        arquivo_excel = openpyxl.load_workbook(caminho_arquivo)
        planilha = arquivo_excel[nome_planilha]
        return planilha
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")
    except KeyError:
        print(f"Planilha {nome_planilha} não encontrada no arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar a planilha: {e}")
    return None

def exibir_tabela(planilha):
    tabela = [linha for linha in planilha.iter_rows(values_only=True)]
    print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

def vizualizar_planilha():
    caminho_arquivo = input("Informe o caminho do arquivo Excel: ")
    nome_planilha = input("Informe o nome da planilha: ")
    planilha = carregar_planilha(caminho_arquivo, nome_planilha)
    if planilha:
        exibir_tabela(planilha)

if __name__ == "__main__":
    vizualizar_planilha()