from time import sleep 
print('-=' * 20)
print('{:=^40}'.format('Quiz'))
print('-=' * 20)
#Pergunta 1
print('Qual a capital do Brasil ? ')
print('(A)-Brasilia\n(B)-Salvador\n(C)-São Paulo')
resp = str(input('Qual a sua resposta? ')).strip()
print('PROCESSANDO...')
sleep(1)
if resp.title() == 'A':
    print('Parabéns você acertou!!')
else:
    print('Você errou!!')
print('...')
sleep(1)
print('-=' * 20)
#Pergunta 2
print('O Brasil é um país de qual continente? ')
print('(A)-Europa\n(B)-Asia\n(C)-América')
resp2 = str(input('Qual a sua resposta? ')).strip()
print('PROCESSANDO...')
sleep(1)
if resp2.title() == 'C':
    print('Parabéns você acertou!!')
else:
    print('Você errou!!')
print('...')
sleep(1)
print('-=' * 20)
#Pergunta 3
print('Qual o satélite natural da terra? ')
print('(A)-A própia terra\n(B)-A Lua\n(C)-O Sol')
resp3 = str(input('Qual a sua resposta? ')).strip()
print('PROCESSANDO...')
sleep(1)
if resp3.title() == 'B':
    print('Parabéns você acertou!!')
else:
    print('Você eroou!!')
print('...')
sleep(1)
print('-=' * 20)
#pergunta 4
print('A lua possui luz própia? ')
print('(A)-Sim\n(B)-Não\n(C)-Apenas de noite')
resp4 = str(input('Qual a sua resposta? ')).strip()
print('PROCESSANDO...')
sleep(1)
if resp4.title() == 'B':
    print('Parabéns você acertou!!')
else:
    print('Você errou!!')
print('...')
sleep(1)
print('-=' * 20)
#Pergunta 5
print('Os cachorros fazem parte de qual familia animal?')
print('(A)-Caninos\n(B)-Equinos\n(C)-Felinos')
resp5 = str(input('Qual a sua resposta? ')).strip()
print('PROCESSANDO')
sleep(1)
if resp5.title() == 'A':
    print('Parabéns você acertou!!')
else:
    print('Você errou!!')
print('...')
sleep(1)
print('-=' * 20)
#Pergunta 6
print('O que os ursos fazem no periodo de inverno?')
print('(A)-Vão para um lugar mais quente\n(B)-Comem mais mel\n(C)-Hibernam')
resp6 = str(input('Qual a sua resposta? ')).strip()
print('PROCESSANDO...')
sleep(1)
if resp6.title() == 'C':
    print('Parabéns você acertou!!')
else:
    print('Você errou!!')
print('-=' * 20)
print('{:=^40}'.format('FIM'))
print('-=' * 20)







