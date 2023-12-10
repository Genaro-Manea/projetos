# tupla com 10 palavras, scanear as vogais e imprimir as palavras e suas vogais

palavras = ('Bola', 'Viga', 'Codorna', 'Computador', 'Diagrama', 'Outono',
            'Automovel', 'Algoritmos', 'Noite', 'Orador')
vogais = 'aeiouAEIOU'
result = []

for p in palavras:
    print('\nNa palavra {} temos as vogais: ' .format(p.upper()), end='')
    for letra in p:
        if letra in 'aeiouAEIOU':
            print(letra.upper(), end=' ')