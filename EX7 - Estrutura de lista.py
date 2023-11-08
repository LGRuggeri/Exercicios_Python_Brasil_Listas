# 7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import math

lista_numeros= []

print('Digite 5 números positivos inteiros, para apresentar a soma, a multiplicação e os números.')
for i in range(5):
    numeros= int(input(f'Digite o {i+1} número: '))
    lista_numeros.append(numeros)

soma_numeros= sum(lista_numeros)
multiplicacao_numeros= math.prod(lista_numeros)
print('A soma dos números é: ', soma_numeros)
print('A multiplicação dos números é: ', multiplicacao_numeros)
print('Os números informados foram: ', lista_numeros)