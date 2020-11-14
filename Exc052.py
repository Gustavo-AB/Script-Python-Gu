num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('Esse numero é PRIMO!!')
    else:
        print('Esse número não é PRIMO!!')