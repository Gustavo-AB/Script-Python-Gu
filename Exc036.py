vcasa = float(input('Qual o valor da casa? '))
vsal = float(input('Qual é o valor do seu salario? '))
qanos = float(input('Em quantos anos você deseja pagar? '))
pres = vcasa / (qanos * 12)
sal = vsal * 30 / 100
if pres <= sal:
    print('o emprestimo foi APROVADO!!')
    print('As prestações serão de R${:.2f} por mês!'.format(pres))
else:
    print('O emprestimo foi NEGADO!!')
    print('As prestações de R${} por mês, está muito próxima, do valor do seu salário!!'.format(pres))