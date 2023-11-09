# 11.Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

import random
from itertools import chain


numeros1= random.sample(range(1,30),5)
numeros2= random.sample(range(31,50),5)
numeros3= random.sample(range(51,100),5)
lista_ramdom1= list(numeros1)
lista_ramdom2= list(numeros2)
lista_ramdom3= list(numeros3)

print('A lista 1 é: ' ,lista_ramdom1)
print('A lista 2 é: ' ,lista_ramdom2)   
print('A lista 2 é: ' ,lista_ramdom3)


lista_intercalada1= chain.from_iterable(zip(lista_ramdom1,lista_ramdom3))
lista_intercalada2= chain.from_iterable(zip(lista_ramdom2,lista_ramdom3))
lista_intercalada3= chain.from_iterable(zip(lista_ramdom1,lista_ramdom2))
print('A primeir lista de 10 vetores intercalados é:\n ' ,*lista_intercalada1)
print('A segiunda lista de 10 vetores intercalados é:\n ' ,*lista_intercalada2)
print('A terciera lista de 10 vetores intercalados é:\n ' ,*lista_intercalada3)