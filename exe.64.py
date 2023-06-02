cont = soma = num = 0
num = int(input('Digite um numero: [999 para parar] '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um numero: [999 para parar] '))
print('VOCÊ DIGITOU {} NÚMEROS'.format(cont))
print('-=-' * 20)
print('A SOMA ENTRE OS NÚMEROS FOI {}'.format(soma))