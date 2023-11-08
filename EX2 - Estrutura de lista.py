# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import random

lista_numeros_ramdom= []

numeros_ramdom= random.sample(range(1,100),10)
print(numeros_ramdom)
lista_numeros_ramdom.append(numeros_ramdom)

for i in lista_numeros_ramdom:
    print(i[::-1])
