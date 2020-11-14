from datetime import date
print('-=' * 20)
print('{:=^40}'.format(' BISSEXTO OU NÃO ? '))
print('-=' * 20)
ano = int(input('Digite qualquer ano, para saber se é bissexto ou não. Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é SIM BISSEXTO!!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!!'.format(ano))



