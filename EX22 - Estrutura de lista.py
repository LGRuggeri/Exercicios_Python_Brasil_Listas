# 22.Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
# com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, 
# testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento.
# O programa deverá receber um número indeterminado de entradas, 
# cada uma contendo um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; 
# necessita troca do cabo ou conector; 
# quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa. 
# Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

import os

necessita_esfera= 0
necessita_limpeza= 0
necessita_cabo_conector= 0
necessita_quebrado_inutilizado= 0
continuar= True
espaco= ' '

while continuar != 2:
    esfera= int(input('Necessita manutenção na esfera? 1-Sim ou 2-Não: '))
    limpeza= int(input('Necessita limpeza? 1-Sim ou 2-Não: '))
    cabo_conector= int(input('Necessita troca do cabo ou conector? 1-Sim ou 2-Não: '))
    quebrado_inutilizado= int(input('Quebrado ou inutilizado? 1-Sim ou 2-Não: '))
    clear= lambda: os.system('cls')
    if esfera == 1:
        necessita_esfera+=1
    if limpeza == 1:
        necessita_limpeza+=1
    if cabo_conector == 1:
        necessita_cabo_conector+=1
    if quebrado_inutilizado == 1:
        necessita_quebrado_inutilizado+=1
    continuar= int(input('Deseja continuar preechendo? 1-Sim ou 2-Não: '))
    clear()
        
clear()
total= (necessita_esfera+necessita_limpeza+necessita_cabo_conector+necessita_quebrado_inutilizado)
print('Quantidade mouses:',total)
print('Situação',espaco*35,'Quantidade',espaco*4,'percentual')
print('1 - necessita da esfera ',espaco*23,necessita_esfera,espaco*12,round((necessita_esfera/total)*100),'%')
print('2 - necessita de limpeza',espaco*23,necessita_limpeza,espaco*12,round((necessita_limpeza/total)*100),'%')
print('3 - necessita troca do cabo ou conector',espaco*8,necessita_cabo_conector,espaco*12,round((necessita_cabo_conector/total)*100),'%')
print('4 - quebrado ou inutilizado ',espaco*19,necessita_quebrado_inutilizado,espaco*12,round((necessita_quebrado_inutilizado/total)*100),'%')