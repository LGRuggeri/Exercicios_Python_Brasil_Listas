# 19.Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a 
# uma grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e 
# informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado 
# o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para 
# o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual 
# de cada um dos concorrentes e informar o vencedor da enquete. 
# O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

import os
import time
sistema_operacional= ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
cod_sistema_operacional= [1,2,3,4,5,6]
votos= [0,0,0,0,0,0]
percentagem= []
pesquisa=True

while pesquisa != 0:
    print('Qual o melhor Sistema Operacional para uso em servidores?')
    pesquisa= int(input('1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\nResposta:'))
    if pesquisa == 0:
        break
    elif pesquisa >= 7:
        print('Valor digitado inválido, digitar novamente um valor válido!!!')
        time.sleep(2)
    else:
        for i in range(len(cod_sistema_operacional)):
            if pesquisa == cod_sistema_operacional[i]:
                votos[i] +=1
    time.sleep(1)
    clear= lambda: os.system('cls')
    clear()

clear()

print_sistema = ("Sistema Operacional")
espaco1 = "      "
espaco2 = "   "
print_votos = "Votos"
print_total = "Total"
print(print_sistema, espaco1, print_votos, " " * (len(espaco2) * 2), "%")
print("-" * len(print_sistema), espaco1, "-" * len(print_votos), espaco2, "-" * 7)
for i,sistema in enumerate(sistema_operacional):
    if votos[i] == 0:
        print(sistema_operacional[i],  
          " " * (len(print_sistema) - len(sistema_operacional[i]) + len(print_votos) + 3),
          votos[i]," ",espaco1,votos[i],"%")
    else: 
        calc_percentual=(round(votos[i] / sum(votos) * 100))
        percentagem.append(calc_percentual)
        print(sistema_operacional[i],  
          " " * (len(print_sistema) - len(sistema_operacional[i]) + len(print_votos) + 3),
          votos[i]," ",espaco1,percentagem[i],"%")
        
print("-" * len(print_sistema), espaco1, "-" * len(print_votos))

print(print_total, " ",espaco1 * 3," ",sum(votos),'\n')   
indice_ganhador= votos.index(max(votos))
percentagem_final= (round(max(votos)/sum(votos)*100))
print(f'O Sistema Operacional mais votado foi {sistema_operacional[indice_ganhador]} , com {votos[indice_ganhador]} votos, correspondendo a {percentagem_final}% dos votos')