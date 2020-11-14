tempo = int(input('Quantos anos tem o seu carro ? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
#condição simples
ntemp = int(input('Quantos anos tem sua moto ? '))
print('Moto nova' if ntemp <=3 else 'Moto velha')
print('--FIM--')
nome = str(input('Qual é o seu nome ? '))
if nome == 'Gustavo':
    print('Bom dia, {}\nQue nome incrivelmente bonito você tem !'.format(nome))
else:
    print('Que nome legalzinho você tem !')
print('Bom dia {} !'.format(nome))
nota1 = float(input('Qual foi sua primeira nota ? '))
nota2 = float(input('Qual foi sua segunda nota ? '))
media = (nota1 + nota2)/2
if media >=6:
    print('PARABÉNS! Sua média foi {} '.format(media))
else:
    print('Sua média foi {}! ESTUDE MAIS!'.format(media))


