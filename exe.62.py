print('PROGRESSÃO ARITMETICA')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('-> {}'.format(termo), end=' ')
        cont += 1
        termo = termo + razão
    print('PAUSA')
    mais = int(input('Quantos termso ainda quer mostrar ? '))
print('Progressãofinalizada, com {} termos'.format(total))