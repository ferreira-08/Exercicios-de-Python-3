from random import randint
computador = randint(0, 10)
print('Eu pensei em um número de 0 até 10')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite ? '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente')
        elif jogador > computador:
            print('Menos...Tente novamente')
print('Parabéns, acertou com {} PALPITES VAGABUNDO '.format(palpite))
