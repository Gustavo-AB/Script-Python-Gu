from time import sleep
print('-=' * 20)
print('{:=^40}'.format('80KM'))
print('-=' * 20)
vel = float(input('Qual a velocidade do carro? '))
mult = vel - 80
valor = mult * 7
if vel <=80:
    print('-=' *20)
    print('Tenha um bom dia! Dirija com segurança!!')
else:
    print('LIMITE DE VELOCIDADE ULTRAPASADO\nGERANDO MULTA...')
    sleep(2)
    print('-=' * 20)
    print('Você ultrapassou o limite de velocidade!!')
    print('Você passou a {}Km acima do limite, devera pagar uma multa no valor de R${}'.format(mult, valor))
print('-=' * 20)