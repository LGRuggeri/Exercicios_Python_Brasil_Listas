# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista_notas= []

for i in range(4):
    notas= float(input(f'Professor informa a {i+1} nota do aluno: '))
    lista_notas.append(notas)

media_notas= sum(lista_notas)/4
print(f'As notas do aluno foram {lista_notas} e a média foi {media_notas}')