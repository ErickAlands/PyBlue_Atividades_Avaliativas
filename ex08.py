#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um 
#dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve 
#contribuir por 35 anos para se aposentar.
import datetime
anoAtual = datetime.datetime.now().year
dados = dict()
dados['Nome'] = str(input('Informe seu nome: '))
dados['Ano de Nascimento'] = int(input('Informe seu ano de nascimento: '))
dados['Idade'] = (anoAtual - dados['Ano de Nascimento'])
dados['CTPS'] = int(input('Informe o número de sua CTPS (digite 0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Informe o ano em que foste contratado: '))
    dados['Salário'] = float(input('Informe seu salário: '))
    dados['Idade de Aposentadoria'] = ((dados['Ano de Contratação'] - dados['Ano de Nascimento']) + 35)
    print(dados)
else:
    print(dados)
