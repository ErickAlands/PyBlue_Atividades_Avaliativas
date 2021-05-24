    #04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma 
    #string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a 
    #data seja inválida.
data = str(input('Digite uma data (DD/MM/AAAA): ')) #data que o usuário vai inserir
dia, mes, ano = map(int, data.split('/')) #variavel para dia, mês e ano (junto)
def dataExtenso(dia, mes, ano): #função para validar a data escrita por extenso
    if validarData(dia, mes, ano) == False: #validador para caso seja inserida uma data inválida pelo usuário
        return 'Data Inválida'
    mm = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] #lista dos meses em extenso para ser puxado logo mais
    return f'{dia} de {mm[mes-1]} de {ano}' #encerra a função, devolvendo os valores resultantes para onde a função foi chamada
def validarData(dia, mes, ano): #validar se a data existe/é possível
    if dia < 0 or dia > 31 or mes < 0 or mes > 12 or ano < 0 or ano > 999999999999: #validador para retirar datas impossíveis, como dia 40 ou mês 20
        return False #retorna o False para o primeiro 'if' do validarData
    elif mes in (4, 6, 9, 11) and dia > 30: #validar que os meses 4, 6, 9 e 11 não tenham mais de 30 dias
        return False
    elif mes == 2 and ano % 4 != 0 and dia > 28: #validar que fevereiro não tenha mais do que 28 dias
        return False
    elif mes == 2 and ano % 4 == 0 and ano  % 100 != 0 or ano % 400 and dia > 29: #validar ano bisexto
        return False
print(dataExtenso(dia, mes, ano))
