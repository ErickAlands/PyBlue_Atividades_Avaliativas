   #06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
      # "Telefonou para a vítima?"
      # "Esteve no local do crime?"
      # "Mora perto da vítima?"
      # "Devia para a vítima?"
      # "Já trabalhou com a vítima?" 
   # O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
      # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
      # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
      # Caso contrário, ele será classificado como "Inocente".
respostas = ['N', 'N', 'N', 'N', 'N'] #lista de respostas
perguntas = ['Você telefonou para a vítima? ', 'Você esteve no locar do crime? ', 'Você mora perto da vítima? ', 
'Você devia para a vítima? ', 'Você já trabalhou com a vítima? '] #lista de perguntas
for i in range(0,5): #função para cobrir as 5 perguntas
   respostas[i] = input(perguntas[i]).upper().capitalize() #respostas do usuário, tornando a letra maiúscula e pegando somente a primeira letra
if respostas.count('S') == 2: #validador das respostas, contando e adicionando todas as respostas S na lista
   print('Você é um(a) Suspeito(a)!')
if respostas.count('S') <= 4:
   print('Você é um(a) Cúmplice!')
if respostas.count('S') == 5:
   print('Você é o(a) Assassino(a)!')
