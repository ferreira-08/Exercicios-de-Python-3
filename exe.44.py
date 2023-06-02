print(' LOJAS FERREIRAS ')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro / cheque
[ 2 ] a vista no cartão
[ 3 ] 2 vezes no cartão sem juros
[ 4 ] 3 vezes ou mais no cartão com 20% de juros''')
opção = int(input('Digite sua opção'))
if opção == 1:
    desconto = preço - (preço * 10) / 100
    print('O valor total co desconto será {:.2f}'.format(desconto))
elif opção == 2:
    desconto = preço - (preço * 5 / 100)
    print('O valor total com desconto, será {:.2f} '.format(desconto))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('O valor total será parcelado em 2x de R${} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas ? '))
    parcela = total / totparc
    print('Sua compra  será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('OPÇÃO INVÁLIDA')
