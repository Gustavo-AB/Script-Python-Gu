soma = 0
maiori = 0
nomemaior = ''
nomemenor = ''
menori = 0
contm = 0
contf = 0
conti = 0
print('{:=^40}'.format('CADASTRO DE CASA'))
qdpes = int(input('Quantas pessoas tem em sua casa? '))
for c in range(1, qdpes+1):
    print('=' * 40)
    nome = str(input('{}ªPessoa. Nome: '.format(c))).strip().upper()
    idade = int(input('{}ªPessoa. Idade: '.format(c)))
    sexo = str(input('{}ªPessoa. Sexo M/F: '.format(c))).strip().upper()
    soma += idade
    media = soma / qdpes
    if sexo in 'Mm':
        contm += 1
    if sexo in 'Ff':
        contf += 1
    if c == 1:
        maiori > idade
    else:
        if idade > maiori:
            maiori = idade
            nomemaior = nome
    if c == 1 and menori < idade:
        idade < menori
        menori = idade
        nomemenor = nome
print('=' * 40)
print('A média da idade da família é {:.0f} anos!'.format(media))
print('-' * 40)
print('São {} homem(s) e {} mulher(s)! '.format(contm, contf))
print('-' * 40)
if idade == idade:
    conti += 2
    idade = idade
    print('{} pessoas tem a mesma idade!'.format(conti))
else:
    print('{} é mais velho(a) e tem {} anos!'.format(nomemaior, maiori))
print('{} é mais novo(a) e tem {} anos!'.format(nomemenor, menori))
print('-' * 40)

print('=' * 40)