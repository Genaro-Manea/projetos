def dimensoesObjeto():
    while True: # loop infinito até executar o "finally"
        try:
            altura = float(input('Entre com a altura do ojeto (cm): '))
            comprimento = float(input('Entre com comprimento do ojeto (cm): '))
            largura = float(input('Entre com a largura do ojeto (cm): '))
            volume = altura * comprimento * largura
            global valor # definindo como global para utilizar a variável no programa principal
            if volume <= 0: # tratamento de valor inválido
                print('Você declarou alguma medida incorretamente.')
                print('Por favor, entre com as medidas do objeto')
                return dimensoesObjeto() # recomeça a coleta das informações do objeto
            elif volume > 0 and volume < 1000:
                valor = 10
            elif volume >= 1000 and volume < 10000:
                valor = 20
            elif volume >= 10000 and volume < 30000:
                valor = 30
            elif volume >= 30000 and volume < 100000:
                valor = 50
            else:  # tratamento de valor inválido
                print('O volume do objeto é de {:.2f}cm³.'.format(volume))
                print('Só transportamos volumes inferiores a 100000cm³')
                print('Por favor, entre com as medidas do objeto')
                return dimensoesObjeto()
            print('O volume do objeto é de {:.2f}cm³.'.format(volume))
        except ValueError: # tratamento de valor não numérico
            print('Você declarou uma medida do objeto com valor não numérico.')
            print('Por favor, entre com as medidas do objeto.')
            return dimensoesObjeto()
        finally:
            break
def pesoObjeto():
    while True:
        try:
            peso = float(input('Entre com o peso do objeto (kg): '))
            global multiPeso # para utilizar a variável no programa principal
            if peso <= 0:  # tratamento de valor inválido
                print('Você digitou um valor inválido.')
                print('Por favor, entre com ao peso do objeto')
                return pesoObjeto()
            elif peso > 0 and peso < 0.1:
                multiPeso = 1
            elif peso >= 0.1 and peso < 1:
                multiPeso = 1.5
            elif peso >= 1 and peso < 10:
                multiPeso = 2
            elif peso >= 10 and peso < 30:
                multiPeso = 3
            else:  # tratamento de valor inválido
                print('Só transportamos volumes inferiores a 30 kg')
                return pesoObjeto()
        except ValueError: # tratamento de valor não numérico
            print('Você declarou o peso do objeto com valor não numérico.')
            print('Por favor, entre com o peso do objeto.')
            return pesoObjeto()
        finally:
            break
def rotaObjeto():
    while True:
        try:
            rota = input('Escolha a rota para o transporte do volume:\n'
                             'RS - Do Rio de Janeiro até São Paulo\n'
                             'SR - De São Paulo até o Rio de Janeiro\n'
                             'BS - De Brasília até São Paulo\n'
                             'SB - De São Paulo até Brasília\n'
                             'BR - De Brasília até o Rio de Janeiro\n'
                             'RB - Do Rio de Janeiro até Brasília\n'
                             '')
            rota = str.upper(rota) # converter a variável em caixa alta
            global multiRota # para utilizar a variável no programa principal
            if rota == 'RS':
                multiRota = 1
            elif rota == 'SR':
                multiRota = 1
            elif rota == 'BS':
                multiRota = 1.2
            elif rota == 'SB':
                multiRota = 1.2
            elif rota == 'BR':
                multiRota = 1.5
            elif rota == 'RB':
                multiRota = 1.5
            else:  # tratamento de valor inválido
                print('Você digitou uma rota que não existe.')
                print('Por favor, selecione a rota novamente.')
                return rotaObjeto()
        finally: # não utilizei "except" pois a variável trabalha com caracteres
            break
# programa principal
print('Bem-vindo à Companhia de Logística Genaro Manea LTDA.') # identificação
#chamando as funções
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
# retornando ao usuário o total a ser pago
print('Total a pagar: R$ {:.2f} (dimensões: {:.2f} * peso: {:.1f} * rota: {:.1f}).' .format(valor * multiPeso * multiRota, valor, multiPeso, multiRota))