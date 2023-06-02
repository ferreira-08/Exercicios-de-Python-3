while True:
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo ? [M/F]')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM')
