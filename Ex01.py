   #01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   #A soma deles;
   #A multiplicação entre eles;
   #A divisão inteira deles;
   #Mostre na tela qual é o maior;
   #Verifique se o resultado da soma é par ou impar e mostre na tela;
   #Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o 
   #resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
num1 = float(input('Digite um número: ').replace(',','.')) #primeiro número do usuário
num2 = float(input('Digite outro número: ').replace(',','.')) #segundo número do usuário
print(f'\nA soma de {num1:.1f} e {num2:.1f} é {num1+num2:.1f}\n') #soma dos dois números informados
print(f'A multiplicação entre {num1:.1f} e {num2:.1f} é {num1*num2:.1f}\n') #multiplicação entre os números informados
print(f'A divisão inteira entre {num1:.1f} e {num2:.1f} é {num1//num2:.1f}\n') #divisão inteira entre os números informados
if num1 > num2: #validação para descobrir o maior número
    print(f'O maior número é {num1}\n')
elif num2 > num1:
    print(f'O maior número é {num2}\n')
else:
    print('Os números são iguais!')
if (num1+num2) % 2 == 0: #validação para descobrir se o resultado da soma é par ou impar
    print('O resultado da soma é um número PAR!\n')
else:
    print('O resultado da soma é um número IMPAR!\n')
if (num1*num2) >= 40: #validação para a descobrir se a multiplicação entre os dois números foi maior do que quarenta e aplicar a condição imposta na questão.
    if num1 < num2:
        print(f'O resultado da divisão inteira entre {num1} e {num2} é igual a 0.') #se o resultado da divisão inteira for 0, quebraria o código na fórmula abaixo.
    else:
        print(f'O resultado da divisão inteira sobre o resultado da multiplicação entre {num1} e {num2} é {(num1*num2)/(num1//num2)}\n')
else:
    print(f'O resultado da multiplicação entre {num1} e {num2} não foi maior que 40.')
