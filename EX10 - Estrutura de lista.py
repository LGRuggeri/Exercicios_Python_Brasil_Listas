# 10.Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores.

import random
from itertools import chain


numeros1= random.sample(range(1,30),10)
numeros2= random.sample(range(31,50),10)
lista_ramdom1= list(numeros1)
lista_ramdom2= list(numeros2)

print('A lista 1 é: ' ,lista_ramdom1)
print('A lista 2 é: ' ,lista_ramdom2)


lista_intercalada= chain.from_iterable(zip(lista_ramdom1,lista_ramdom2))
print('A lista de 20 vetores intercalados é:\n ' ,*lista_intercalada)