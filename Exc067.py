while True:
    print('=-' * 20)
    tabu = int(input('Deseja ver a tabúada de qual valor? '))
    if tabu <= 0:
        break
    for tab in range(1, 11):
        print(f'{tabu} X {tab:2} = {tab*tabu:2}')
print('FIM!')