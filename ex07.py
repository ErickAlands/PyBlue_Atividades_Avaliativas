#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem 
#crescente.
lista = []
par = []
impar = []
for n in range (0,7):
    numeros = int(input('Informe um número inteiro: '))  
    if numeros % 2 == 0:
        par.append(numeros)
    elif numeros % 2 != 0:
        impar.append(numeros)
par.sort()
impar.sort()
lista = [par] + [impar]
print(lista)
