# 24.Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
# simulando os lançamentos dos dados.

import random
contador= []
numeros_sorteados= []
cont_dado_1= 0
cont_dado_2= 0
cont_dado_3= 0
cont_dado_4= 0
cont_dado_5= 0
cont_dado_6= 0

for i in range(100):
    dados_lancados= random.randrange(1,7)
    numeros_sorteados.append(dados_lancados)
    
for i,valor in enumerate(numeros_sorteados):
    dado_lado= numeros_sorteados[i]
    if dado_lado == 1:
        cont_dado_1+=1
    elif dado_lado == 2:
        cont_dado_2+=1
    elif dado_lado == 3:
        cont_dado_3+=1
    elif dado_lado == 4:
        cont_dado_4+=1
    elif dado_lado == 5:
        cont_dado_5+=1
    else:
        cont_dado_6+=1
    
contador.append(cont_dado_1)
contador.append(cont_dado_2)
contador.append(cont_dado_3)
contador.append(cont_dado_4)
contador.append(cont_dado_5)
contador.append(cont_dado_6)

for i in range(len(contador)):
    print(f'Quantidade de vezes que o lado do número {i+1} saiu foi: ',contador[i])