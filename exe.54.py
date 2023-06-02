from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu ?? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
        print('MAIOR DE IDADE')
    else:
        totmenor += 1
        print('MENOR DE IDADE')
print('Tem {} pessoas MAIORES DE IDADE'.format(totmaior))
print('Tem {} pessoas MENORES DE IDADE'.format(totmenor))