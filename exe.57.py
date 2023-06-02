sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos, digite novamente ')).strip().upper()[0]
print('Sexo {} foi cadastrado com sucesso '.format(sexo))
