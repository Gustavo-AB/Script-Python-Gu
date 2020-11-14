print('-=' * 20)
print('{:=^40}'.format('ALISTAMENTO MILITAR'))
print('-=' * 20)
idade = int(input('Em que ano você nasceu? '))
if idade == 2002:
    print('Neste ano voçê completa 18 anos de idade!!\nEstá na hora de se ALISTAR!!')
elif idade > 2002:
    trest = idade - 2002
    print('Você tem {} anos, ainda faltam {} anos para seu alistamento, que será em {}!!'.format(2020 - idade, trest, trest + 2020))
else:
    saldo = idade + 18
    print('O seu alistamento foi em {}!! E já se passaram {}!!'.format(saldo, 2020 - saldo))
    print('Você esta com {} anos, se ainda não se alistou ALISTE-SE IMEDIATAMENTE!!'.format(2020 - idade))
print('-=' * 20)
print('{:=^40}'.format('Ministério da Segurança Publica'))
print('-=' * 20)
