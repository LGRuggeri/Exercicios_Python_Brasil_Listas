# 18.Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para
# saber qual o melhor jogador após cada jogo.
# Para isto, faz-se necessário o desenvolvimento de um programa, 
# que será utilizado pelas telefonistas, para a computação dos votos.
# Sua equipe foi contratada para desenvolver este programa, 
# utilizando a linguagem de programação Python.
# Para computar cada voto, a telefonista digitará um número,
# entre 1 e 23, correspondente ao número da camisa do jogador. 
# Um número de jogador igual zero, indica que a votação foi encerrada.
# Se um número inválido for digitado, o programa deve ignorá-lo,
# mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
# Após o final da votação, o programa deverá exibir:
    
# a.O total de votos computados;
# b.Os números e respectivos votos de todos os jogadores que receberam votos;
# c.O percentual de votos de cada um destes jogadores;
# d.O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos 
# e o percentual de votos dados a ele.

# Observe que os votos inválidos e o zero final não devem ser computados como votos.
# O resultado aparece ordenado pelo número do jogador. 
# O programa deve fazer uso de arrays. 
# O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
# Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
# A função calculará o percentual e retornará o valor calculado. 
# A disposição das informações deve ser o mais próxima possível ao exemplo. 
# Os dados são fictícios e podem mudar a cada execução do programa. 
# Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em
# um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
# Abaixo segue uma tela de exemplo. 
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

import os

numeros_jogadores= [1,2,3,4,5,6,7,8,9,10,
                    11,12,13,14,15,16,17,
                    18,19,20,21,22,23]

votos= [0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0]

votacao= True

while votacao != 0:
    voto= int(input('Informe o número do jogador a ser votado, sendo de 1 há 23 ou zero para encerrar: '))
    if voto == 0:
        break
    elif voto >= 24:
        print('O número informado é inválido, por favor digitar novamente!!!')
    else:
        for i in range(len(numeros_jogadores)):
            if voto == numeros_jogadores[i]:
                votos[i] += 1

clear = lambda: os.system('cls')
clear()

for i, numero in enumerate(numeros_jogadores):
    if votos[i] > 0:
        print(f'O jogador número {numero} teve: {votos[i]} voto(s)')

print('Resultado da votação:')
print(f'Foram computados {sum(votos)} voto(s). ')

print('Jogador  Votos  %')
for i,numero in enumerate(votos):
    if numero == 0:
        percentual_votos= 0
    else:
        percentual_votos= (votos[i]/sum(votos))*100
        print(f'  {i+1}      {numero}     {round(percentual_votos)}%')