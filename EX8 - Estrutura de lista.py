# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu 
# respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

lista_idade= []
lista_altura= []
count= 0

print('Digite a idade e a altura das pessoas.')
while count <= 4:
    idade= int(input(f'Digite a idade da {count+1} pessoa:'))
    lista_idade.append(idade)
    altura= int(input(f'Digite a altura da {count+1} pessoa:'))
    lista_altura.append(altura)
    count+=1

for i in range(1):
        print(lista_idade[::-1])
        print(lista_altura[::-1])
