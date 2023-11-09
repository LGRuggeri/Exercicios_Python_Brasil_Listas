# 12.Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos 
# possuem altura inferior à média de altura desses alunos.

count= 0
idade_alunos= []
idade_alunos_13= []
altura_alunos= []
abaixo_da_media= []

while count <= 29:
    altura_aluno= altura_alunos.append(int(input(f'Digite a altura do {count+1} aluno: ')))
    idade_aluno= int(input(f'Digite a idade do {count+1} aluno: '))
    if idade_aluno > 13:
        idade_alunos_13.append(idade_aluno)
    idade_alunos.append(idade_aluno)
    count+=1
    
media_altura= int(sum(altura_alunos)/len(altura_alunos))

for i in range(len(idade_alunos_13)):
    if idade_alunos_13[i] < media_altura:
        abaixo_da_media.append(idade_alunos_13[i])
        
print(f'Temos um total de {len(abaixo_da_media)} aluno(s) com mais de 13 anos a baixo da média de altura.')                