#Primeiro eu pergunto o valor a ser sacado
valor = int(input('Qual o valor a ser sacado R$? '))
#Depois eu crio um total que vai receber o valor da variavel Valor
total = valor
#crio uma variavel contendo o valor maximo da cedulas q vou trabalhar
ced = 50
#e crio um contador de cédulas
totced = 0

#crio uma repetição infinita que vai ir tirando os valores da cedulas até zerar olhe para entender
while True:
    # se o meu total for maior ou igual que o valor da minha cedula o total vai receber ele mesmo menos o valor da cedula e vai ir tirando no caso 50 até nao dar mais ai coloco o contador de cedula para ir contando quantas cedulas eu tirei
    if total >= ced:
        total -= ced
        totced += 1
    else:
        #isso é se o contador de cedulas for maior que 0 ai ele printa  é mais para deixar bonito
        if totced > 0:
            print(f'Total de {totced} Cédulas de {ced}')
        #aqui se a cedula for igual a 50 como esta mostrando ai ela passa a valer a proxima cedula com valor menor no caso o 20 e assim por diante
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        # quando o total for igual a 0 no caso quando o dinheiro acabar o programa acaba tambem com um brake
        if total == 0:
            break
        

         