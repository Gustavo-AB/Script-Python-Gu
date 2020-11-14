mdi = qdh = mmdv = 0

while True:
    print('=' * 30)
    idade = int(input('Digite a Idade: '))
    sexo = ' '


    while sexo not in  'MmFf':
        sexo = str(input('Digite o Sexo [M/F]: ')).strip()
    cont = ' '


    while cont not in 'SsNn':
        cont = str(input('Deseja Continuar [S/N]? ')).strip()

    
    if idade >= 18:
        mdi += 1
    
    if sexo in 'Mm':
        qdh += 1

    if sexo in 'Mm' and idade < 20:
        mmdv += 1

    if cont in 'Nn':
        break


print('=' * 30)
print(f'{mdi} Pessoas São MAIORES de 18 Anos!')
print(f'São {qdh} HOMENS Cadastrados!')
print(f'{mmdv} MULHERES tem MENOS de 20 Anos!')
print('=' * 30)
