maidadeho = 0
nomevelho = ''
meidademu = 0
masc = 0
femi = 0
soma = 0
for da in range(1, 5):
    print('=' * 40)
    nome = str(input('{}ªPessoa. Digite seu nome: '.format(da))).strip().upper()
    idade = int(input('{}ªPessoa. Digite sua idade: '.format(da)))
    sexo = str(input('{}ªPessoa. Digite seu sexo M/F: '.format(da))).strip().upper()
    soma += idade
    media = soma / 4
    if idade == 1 and sexo in 'Mm':
        maidadeho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maidadeho:
        idade > maidadeho
        maidadeho = idade
        nomevelho = nome
    if da == 1 and sexo in 'Ff':
        meidademu = idade
        femi += 1
    if sexo in 'Ff' and idade < 20:
        maidademu = idade
        femi += 1
print('=' * 40)
print('A média das idades é de {:.0f} anos!'.format(media))
print('O homem mais vélho é o {} e tem {} anos!'.format(nomevelho, maidadeho))
print('E {} mulheres ainda NÃO são MAIORES de idade!'.format(femi))
print('=' * 40)