# criar JoKenPô, o usuário escolhe entre 1,2,3 e o programa sorteia 1,2,3.
# armazenar numa lista e retornar os resultados

from random import randint

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1
    elif jogador1 == 2:
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

print('Bem-vindo ao Jokenpô do Genaro Manea!\n\n')

print('1- Pedra\n'
      '2- Papel\n'
      '3- Tesoura\n')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    jog = valida_int('Escolha sua jogada:\n', 0, 3)
    if not jog:
        break
    comp = randint(1,3)
    jogadas.append([jog, comp])
    resultados = vencedor(jog, comp)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Número de vitórias do Jogador 1: {}.' .format(resultados[0]))
print('Número de vitórias do Jogador 2: {}.' .format(resultados[1]))
print('Número de empates: {}.' .format(resultados[2]))