codigo = 0
cadPecas = {}
cadPeca = []

def cadastrarPeca(): # cadastrar as peças
    global cadPecas
    global codigo
    while True:
        codigo += 1 # contador para gerar o código da peça automaticamente
        print('Código do produto: {:0>3}.'.format(codigo))
        cadPecas['Código'] = codigo
        cadPecas['Nome'] = input('Por favor, entre com o NOME da peça: ')
        cadPecas['Nome'] = cadPecas['Nome'].upper()
        cadPecas['Fabricante'] = input('Por favor, entre com o FABRICANTE da peça: ')
        cadPecas['Fabricante'] = cadPecas['Fabricante'].upper()
        cadPecas['Valor'] = input('Por favor, entre com o VALOR da peça: ')
        cadPeca.append(cadPecas.copy())
        break
def consultaCod():
    while True:
        try:
            busca_cod = int(input('Digite o CÓDIGO da peça: '))
            c = busca_cod - 1
            for i, p in enumerate(cadPeca):
                for k, v in p.items():
                    if c == i:
                        print('{} : {}.'.format(k, v))
        except ValueError:
            print('Você digitou uma código com valores não numéricos!')
            continue
        finally:
            break
def consultaFab(): # consultar peças pelo fabricante
    busca_fab = input('Digite o FABRICANTE da peça: ')
    fabricante = [] # lista que será preenchida com as peças do fabricante indicado
    for i, p in enumerate(cadPeca): # busca das peças por fabricante
        for k, v in p.items():
            if busca_fab.upper() == v:
                fabricante.append(cadPeca[i].copy())
    for i, p in enumerate(fabricante): # impressão da lista de peças
        for k, v in p.items():
            print('{} : {}.'.format(k, v))
def consultarPeca(): # consultar as peças cadastradas
    while True:
        consulta = input('Escolha a opção desejada:\n'
                 '1- Consultar Todas as Peças\n'
                 '2- Consultar Peças por Código\n'
                 '3- Consultar Peças por Fabricante\n'
                 '4- Retornar\n'
                 '>>')
        if consulta == '1':
            for p in cadPeca:
                for k, v in p.items():
                    print('{} : {}.'.format(k, v))
            break
        elif consulta == '2':
            consultaCod() # chama a função consultar peças pelo código
            break
        elif consulta == '3':
            consultaFab() # chama a função consultar peças pelo fabricante
            break
        elif consulta == '4':
            break
        else:
            print('Você digitou uma opção inválida!')
            continue
def removerPeca(): # remover peça cadastrada
    while True:
        remover = input('Escolha a opção desejada:\n'
              '1- Remover Peças\n'
              '2- Retornar\n')
        if remover == '1':
            try:
                busca_cod = int(input('Digite o CÓDIGO da peça a ser removida: '))
                c = busca_cod - 1
                for i, p in enumerate(cadPeca):
                    if c == i:
                        del cadPeca[i]
                        print('Peça excluída.')
            except ValueError:
                print('Você digitou uma código com valores não numéricos!')
                continue
            finally:
                break
        elif remover == '2':
            break
        else:
            print('Você digitou uma opção inválida!')
            continue
#programa principal:
print('Bem-vindo ao Controle de Estoque da Bicicletaria do Genaro Manea!')
# menu chamando as funções
while True:
    menu = input('Escolha a opção desejada:\n'
                 '1- Cadastrar Peças\n'
                 '2- Consultar Peças\n'
                 '3- Remover Peças\n'
                 '4- Sair\n'
                 '>>')
    if menu == '1':
        print('Você escolheu a opção Cadastrar Peças:')
        cadastrarPeca()
    elif menu == '2':
        print('Você escolheu a opção Consultar Peças:')
        consultarPeca()
    elif menu == '3':
        print('Você escolheu a opção Remover Peças:')
        removerPeca()
    elif menu == '4':
        print('Muito obrigado pela preferência!\n'
              'Encerrando o programa...')
        break
    else:
        print('Você digitou uma opção inválida!')
        continue