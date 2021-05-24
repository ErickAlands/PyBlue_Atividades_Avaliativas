    #05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne
    #o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
def contaVogais(frase): #função para contar as vogais
    vogais = 0 
    for letra in frase: 
        if letra in ('a', 'e', 'i', 'o', 'u'):
            vogais += 1
    return vogais
def fraseSemVogal(frase): #função para retirar as vogais da frase
    fraseSemVogal = ''
    for letra in frase:
        if letra not in ('a', 'e', 'i', 'o', 'u'):
            if len(fraseSemVogal) == 0 and letra != ' ': 
                fraseSemVogal += letra 
            elif len(fraseSemVogal) != 0: 
                fraseSemVogal += letra
    return fraseSemVogal
frase = str(input('Digite uma frase: ')).lower() 
print(f'A frase digitada tem {contaVogais(frase)} vogais.') 
print(f'A frase sem vogais fica:\n{fraseSemVogal(frase)}.')
