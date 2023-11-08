# 6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média 
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas= []
media_total_alunos= []
count = 0

while count <= 9:
    print(f'Digite as notas do {count+1} aluno.')
    notas.clear()
    for j in range(4):
        notas_aluno= float(input(f'Digite a {j+1} nota: '))
        notas.append(notas_aluno)
    soma_notas= sum(notas)
    media_notas= soma_notas/4
    media_total_alunos.append(media_notas)
    count+=1     
 
j= 0 
for i, notas in enumerate(media_total_alunos):
    if notas >= 7.0:
        j+=1
        print(notas)

print(f'O número de aluno com média maior ou igual que 7 foi de: {j} aluno(s)')