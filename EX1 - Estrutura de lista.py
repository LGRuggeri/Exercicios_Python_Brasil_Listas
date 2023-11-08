# 1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor_inteiros= []

for i in range(5):
    numeros_inteiros= int(input('Digite 5 números inteiros: '))
    vetor_inteiros.append(numeros_inteiros)
    
print('Os números positivos dentro do vetor são: ')
for i, numero in enumerate(vetor_inteiros):
    print(numero)
