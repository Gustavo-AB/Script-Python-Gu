peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu imc é de {:.2f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso!!')
elif imc >=18.5 and imc <= 25:
    print('Você está no peso IDEAL!!')
elif imc >= 25 and imc <= 30:
    print('Você está ACIMA do peso!!')
elif imc >= 30 and imc <= 40:
    print('Você está OBESO!!')
else:
    print('Você está com OBESIDADE MÓRBIDA!!')