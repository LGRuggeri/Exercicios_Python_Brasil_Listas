# 14.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
# ele será classificado como "Inocente".

respostas= []

telefonou_vitimia= respostas.append(int(input('Telefonou para a vítima?, 1- SIM ou 2- NÃO: '))) 
local_crime_vitima= respostas.append(int(input('Esteve no local do crime?, 1- SIM ou 2- NÃO: ')))
mora_perto_vitima= respostas.append(int(input('Mora perto da vítima?, 1- SIM ou 2- NÃO: ')))
devia_vitimia= respostas.append(int(input('Devia para a vítima?, 1- SIM ou 2- NÃO: ')))
trabalhou_vitimi= respostas.append(int(input('Já trabalhou com a vítima?, 1- SIM ou 2- NÃO: '))) 

contador=0
for i, resposta in enumerate(respostas):
    if resposta == 1:
        contador+=1
print(contador)

if contador  <= 1:
     print('Você é inocente do crime. ')
elif contador == 2:
    print('Você é suspeito do crime!')
elif 3 >= contador  or contador <= 4:
    print('Você é Cúmplice do crime!!')
else:
    print('Você é o Assassino do crime!!!')
