r1 = float(input('Qual o raio 1 ?'))
r2 = float(input('Qual o raio 2 ?'))
r3 = float(input('Qual o raio 3'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('TRIANGULO EQUILÁTERO ')
    elif r1 != r2 != r3 != r1:
        print('TRIÂNGULO ESCALENO ')
    else:
        print('TRIÂNGULO ISÓSCELES')
else:
    print('Os segmentos acima NÃO FORMAR UM TRIÂNGULO')