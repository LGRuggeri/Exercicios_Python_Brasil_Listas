# 17.Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
# em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

saltos= []

nome_atleta= input('Informe o nome do atleta: ')
for i in range(5):
    salto_atleta= float(input(f'Informe o {i+1} salto do atleta: '))
    saltos.append(salto_atleta)

media_salto= sum(saltos)/len(saltos)

print('\nAtleta: ', nome_atleta,'\n')
print('Primeiro Salto: ', saltos[0])
print('Segundo Salto: ', saltos[1])
print('Terceiro Salto: ', saltos[2])
print('Quarto Salto: ', saltos[3])
print('Quinto Salto: ', saltos[4],'\n')
print('Resultado final:')
print('Atleta: ', nome_atleta)
print('Saltos:')
for i in range(len(saltos)):
    salto= saltos[i]
    print(salto,'-',end=' ')
print('\nMédia dos saltos: ', media_salto)


