    #02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string 
    #com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
    #depois mostre na tela essa mesma frase sem nenhuma vogal.
frase = str(input('Digite uma frase: ')).lower() #frase digitada pelo usuário
fraseSemVogal = ''
a = e = i = o = u = 0 #variável para vogais
for letra in frase: #loop de repetição para encontrar as vogais
    if letra in ('a'): #condicional para contar as vogais na frase
        a += 1 #contador da vogal a
    elif letra in ('e'):
        e += 1
    elif letra in ('i'):
        i += 1
    elif letra in ('o'):
        o += 1
    elif letra in ('u'):
        u += 1       
    else: #condição para tratar os caracteres que não são vogais
        if len(fraseSemVogal) == 0 and letra != ' ': #garantia que o primeiro caracter não será um espaço
            fraseSemVogal += letra 
        elif len(fraseSemVogal) != 0: #adição do restante dos caracteres
            fraseSemVogal += letra
print(f'A = {a}\nE = {e}\nI = {i}\nO = {o}\nU = {u}\n') #print contando as vogais
print(f'A frase sem vogais fica "{fraseSemVogal}"')
