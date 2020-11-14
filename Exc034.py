print('-=' * 20)
salario = float(input('Qual o salario do funcionario? R$'))
if salario > 1250:
    mul = salario * 10
    div = mul / 100
    nsal = salario + div
    print('Parabéns o funcionário recebeu um aumento de 10%!!\nO funcionario agora recebe R${:.2f}!!'.format(nsal))
if salario <= 1250:
    mul = salario * 15 
    div = mul / 100
    nsal = salario + div
    print('Parabéns o funcionário recebeu um aumento de 15%!!\nEle agora recebe R${:.2f}!!'.format(nsal))
print('-=' * 20)