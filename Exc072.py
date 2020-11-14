numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
'Cinco', 'Seis', 'Sete', 'Oito', 
'Nove', 'Dez', 'Onze', 'Doze', 
'Treze', 'Catorze', 'Quinze', 'Dezesseis', 
'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

#numesc = int(input('Digite um número entre 0 e 20: '))

while True:
    numesc = int(input('Digite um número entre 0 e 20: '))
    if numesc < 0 or numesc > 20:
        print('Erro. tente Novamente!')

    else:
        if numesc >= 0 or numesc <= 20:
            print(f'Você digitou o número {numero[numesc]}!')
            
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if continuar in 'Nn':
        break
print('FIM!')


        