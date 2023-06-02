mediaidade = 0
nomevelho = ''
totmulher20 = 0
somaidade = 0
maioridadehomem = 0

for c in range(1, 5):
    print('-----{}º PESSOA------'.format(c))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Tem {} mulheres ao todo com menos de 20 anos '.format(totmulher20))

