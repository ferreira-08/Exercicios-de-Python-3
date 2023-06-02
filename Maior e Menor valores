x = ........
resp = 'S'
soma =media = maior = menor = quant = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar ? [S/N]'))
media = soma / quant
print('Você digitou {} numeros e a media foi {}'.format(soma, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
