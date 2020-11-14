from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasci = int(input('{}ª Pessoa. Qual o seu ano de nascimento? '.format(pess)))
    atual = date.today().year
    idade = atual - nasci
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoa são SIM maior de idade!'.format(totmaior))
print('{} pessoa NÃO são maior de idade!'.format(totmenor))
