print('SEQUÊCIA DE FIBONACCI')
n = int(input('Qauntos termos você quer ver ??'))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM ')

# 1 - 2 - 3 - 4 - 5 - 6 - 7
#     t1 -t2 -t3
