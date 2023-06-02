# Pergunte o valor da casa
casa = float(input('Digite o valor da casa R$'))
# Salário do comprador
salário = float(input('Qual o seu salário R$ ?'))
# Quantos anos vai pagar
anos = int(input('Quantos anos você vai pagar ?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para comprar uma casa de R$ {}, você terá que pagar R$ {} por mês em {} anos.'.format(casa, prestação, anos))
if prestação <= mínimo:
    print('APROVADO')
else:
    print('NEGADO')
