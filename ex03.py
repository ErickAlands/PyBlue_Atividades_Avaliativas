    #03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar 
    #seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu
    #usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10.
    #O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele 
    #se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites
    #foram necessários para vencer.
from random import randint #gerar valores aleatórios
palpite = 0 #o número que o usuário vai chutar (é 0 para que o usuário possa usar qualquer valor)
tentativas = 0 #o número de tentativas que o usuário precisou para acertar o número
chances = 10 #número de chances disponíveis para o usuário acertar o valor
valor = randint(0,100) #o valor aleatório que o 'robô' vai pensar
senha = str(input('Digite sua senha: ')) # senha para logar no programa
while senha != '12345banana': #validador da senha
    senha = str(input('Senha incorreta! Tente novamente. '))
else: #senha correta, começa o jogo na sequência
    print('Login efetuado com sucesso.\nBem vindo de volta!')
    print('\nVamos jogar o jogo da adivinhação!!!')
    print('\nTente adivinhar o número que estou pensando (entre 0 e 100). Você terá 10 chances para acertar, pense com cuidado!')
    while palpite != valor: #validador do número escolhido pelo usuário
        palpite = int(input('\nQual o número que eu pensei? '))
        tentativas = tentativas + 1 #calcular as tentativas (como começa no 0, o cálculo é ela mesma +1 por casa input do usuário)
        chances = chances - 1 #calcular as chances restantes (mesma coisa que as tentativas, mas é -1 pois é uma contagem regressiva que começa no 10)
        if palpite == valor: #validador caso o palpite seja igual ao valor gerado pelo robô
            print(f'\nParabéns!\nVocê descobriu o número em {tentativas} tentativas! Você ainda tinha {chances} tentativas restantes!\n')
            break #encerra o loop
        else: #validador caso o palpite seja diferente do valor
            if palpite > valor: #validador caso o palpite seja MAIOR que o valor do robô
                print('\nVocê errou! Ai vai uma dica: é um número MENOR!')
            else: #validador caso o palpite seja MENOR que o valor do robô
                print('\nVocê errou! Ai vai uma dica: é um número MAIOR!')
            print(f'\nVocê tem {chances} chances restantes.')
        if chances == 0: #validador caso as chances cheguem a 0
            print('\nSuas chances acabaram! Você perdeu!')
            break
print('Fim de jogo!')
