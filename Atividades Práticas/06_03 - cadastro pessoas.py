# ler nome, ano de nascimento e sexo
# armazenar em dicionário com lista
# apresentar total de cadastros, média de idade, mulheres com menos de 30 e homens acima da média

def menos_30():
    if sexo == 'M' and idade < 30:
        menos30.append[nome]

def acima_media():
    if sexo == 'F' and idade > media:
        acimamedia.append[nome]

cadastro = {'nome':[], 'ano':[], 'sexo':[]}
idade = 2023 - ano
media = (len(cadastro['ano'] * 2023) - sum(cadastro['ano'])) / len(cadastro['ano']
menos30 = []
acimamedia = []

while True:
    terminar = input('Deseja cadastrar mais pessoas? (S/N)')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite "S" para sim ou "N" para não.')
        continue

    nome = input('Qual o nome da pessoa: ')
    ano = int(input('Qual o ano de nascimento: '))
    sexo = input('Qual seu sexo (F/M): ')
    cadastro['nome'].append(nome)
    cadastro['ano'].append(ano)
    cadastro['sexo'].append(sexo.upper())

for item in ano:
    print(item)

print(cadastro)
print('Foram cadastradas {} pessoas.' .format(len(cadastro['ano'])))
print('A média de idade das pessoas cadastradas é: {:.2f} anos.' .format(media)
