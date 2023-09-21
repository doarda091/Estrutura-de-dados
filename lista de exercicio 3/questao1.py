n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
n3 = float(input('Qual sua terceira nota? '))
n4 = float(input('Qual sua quarta nota? '))
n5 = float(input('Qual sua quinta nota? '))

media = (n1 + n2 + n3 + n4 + n5)/5
print(media)

if media >= 7:
    print('Você está aprovado, meus parabéns!!')
else:
    print("Você está reprovado, que pena!!")