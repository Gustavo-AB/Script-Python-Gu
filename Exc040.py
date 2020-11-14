print('-=' * 20)
print('{:=^40}'.format('MÉDIA DO SEMESTRE'))
print('-=' * 20)
nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Parabéns você tirou nota {:.1f} e foi APROVADO!!'.format(media))
elif media >=5 and media <= 6.9:
    print('Você tirou nota {} e esta de RECUPERAÇÃO!!'.format(media))
else:
    print('Você tirou nota {} e esta REPROVADO!!'.format(media))
print('-=' * 20)
print('{:=^40}'.format('UNIVERSIDADE DO COLORADO'))
print('-=' * 20)