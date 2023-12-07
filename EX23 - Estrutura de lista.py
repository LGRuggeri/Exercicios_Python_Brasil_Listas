# 23.A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no
# seu servidor de arquivos. Para tentar resolver este problema, 
# o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
# e identificar os usuários com maior espaço ocupado.
# Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, 
# chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. 
# A partir deste arquivo, você deve criar um programa que gere um relatório, 
# chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, 
# e os dados armazenados em memória, caso sejam necessários, 
# de forma a agilizar a execução do programa. 
# A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através
# de uma função separada, que será chamada pelo programa principal. 
# O cálculo do percentual de uso também deverá ser feito através de uma função, 
# que será chamada pelo programa principal.

from Func_EX23 import *
import os

espaco= ' '
usuarios= ['alexandre','anderson','antonio','carlos','cesar','rosemary']
espaco_bytes= [456123789,1245698456,123456456,91257581,987458,789456125]
espaco_megabytes= []

clear= lambda: os.system('cls')
clear()

for i in range(len(usuarios)):
    print(usuarios[i],espaco_bytes[i])
 
for i in range(len(espaco_bytes)):   
    megabyte= byte_megabyte(espaco_bytes[i])
    espaco_megabytes.append(megabyte)

print('\n')
print('Nr.',espaco,'Usuário',espaco,'Espaço utilizado','','"%" do uso')
for i,valor in enumerate(espaco_megabytes):
    print(i+1,espaco*3,usuarios[i],espaco*5,byte_megabyte(espaco_bytes[i]),'MB'
           ,espaco*3,percentagem_megabyte(espaco_megabytes[i],espaco_megabytes),'%')
    
print('Espaço total ocupado: ', sum(espaco_megabytes),'MB')
media= round(sum(espaco_megabytes)/len(espaco_megabytes),2)
print('Espaço médio ocupado: ', media,'MB')
