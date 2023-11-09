# 13.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média 
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas= []
meses_do_ano= ['Janeiro','Fevereiro','Março',
               'Abril','Maio','Junho','Julho',
               'Agosto','Setembro','Outubro',
               'Novembro','Dezembro']

for i in range(11):
    temperatura= temperaturas.append(int(input(f'Digite a temperatura média de {meses_do_ano[i]} em grau celsius:')))
    
media_temperatura_ano= sum(temperaturas)/len(temperaturas)

print('O mês ou meses que a temperatura ficou acima da média anual: ')

for i in range(len(temperaturas)):
    if temperaturas[i] > media_temperatura_ano:
        print('Mês:',meses_do_ano[i],'com temperatura de:',temperaturas[i],'C°')

     
     