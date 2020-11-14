idade = int(input('Qual o seu ano de nascimento? '))
categoria = 2020 - idade
if categoria <= 9:
    print('Você pertence a categoria MIRIM!!')
elif categoria <= 14:
    print('Você pertence a categoria INFANTIL!!')
elif categoria  <= 19:
    print('Você pertence a categoria JUNIOR!!')
elif categoria <= 25:
    print('Você pertence a categoria SÊNIOR!!')
else:
    print('Você pertence a categoria MASTER!!')
print('Confederação Nacional de Natação!!')