valor = int(input('Digite o valor a ser sacado R$: '))
total = valor
cedula = 100
totced = 0


while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'O total são {totced:.0f} Cédulas de R${cedula:.2f}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
        

