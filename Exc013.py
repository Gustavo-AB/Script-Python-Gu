print('VAMOS CALCULAR 15% DE AUMENTO DE SALARIO ')
salario = (float(input('Qual o valor do salario ? ')))
mu = salario * 15
di = mu / 100
novosalario = salario + di
print('O valor de {}R$ reais com 15% de de aumento, agora vale {}R$ reais \nE teve um aumento de {}R$ reais'.format(salario, novosalario, di))