# 15.Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a 
# -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# a.Mostre a quantidade de valores que foram lidos;
# b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d.Calcule e mostre a soma dos valores;
# e.Calcule e mostre a média dos valores;
# f.Calcule e mostre a quantidade de valores acima da média calculada;
# g.Calcule e mostre a quantidade de valores abaixo de sete;
# h.Encerre o programa com uma mensagem;

numeros= []
numeros_acima_media= []
sair= str(0)

while sair != str(-1):
    numero= numeros.append(int(input('Digite o valor que deseja: ')))
    sair= input('Deseja digitar mais um valor?, digite "-1" para sair ou enter para continuar: ')
    

print('A quantidade de valores foi: ',len(numeros))    

print('Os valores em ordem de digitação:')
for i in range(len(numeros)):
    print(numeros[i], end='')
    print(',', end='')

print('\nOs valores em order inversa de digitação:')
numeros.reverse()
for i in range(len(numeros)):
    print(numeros[i])
    
print('A soma dos valores é: ',sum(numeros))

media_valores= sum(numeros)/len(numeros)
print('A média dos valores é: ',media_valores)

contador_acima_media= 0
for i in range(len(numeros)):
    if numeros[i] > media_valores:
       contador_acima_media+=1 
print('A quantidade de valores acima da média são: ',contador_acima_media)

contador_abaixo_sete=0
for i in range(len(numeros)):
    if numeros[i] < 7:
       contador_abaixo_sete+=1 
print('A quantidade de valores abixo de sete são: ',contador_abaixo_sete)

print('Foco nos objetivos,Força do que é especial,Fé que move montanhas. Lutar sempre, Desistir não existe.')
