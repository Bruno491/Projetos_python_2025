import os
from listas import lista2
from listas import lista3
from listas import lista1

def exibir_menu_departamentos():
    print('<<<<Departamentos>>>>')
    print('1- Departamento 1')
    print('2- Departamento 2')
    print('3- Departamento 3')
    print('4- Voltar')

def obter_opcao():
    try:
        return int(input('Opção: '))
    except ValueError:
        print('Entrada inválida, por favor insira um número.')
        return None

def lista_departamentos():
    while True:
        exibir_menu_departamentos()
        op_dep = obter_opcao()
        
        if op_dep is None:
            continue
        
        os.system('cls')
        
        if op_dep == 1:
            return lista2()
        elif op_dep == 2:
            return lista3()
        elif op_dep == 3:
            return lista1()
        elif op_dep == 4:
            print('Voltando...')
            return None
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    departamento = lista_departamentos()
    if departamento:
        print(f'Departamento selecionado: {departamento}')