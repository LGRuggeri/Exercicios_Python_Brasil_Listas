# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos 
# quadrados dos elementos do vetor.

lista_numeros= []
lista_quadrados= []

for i in range(3):
    numero= int(input(f'Digite o {i+1} número positivo: '))
    lista_numeros.append(numero)
    
for i,numero in enumerate(lista_numeros):
    numero_quadrado= numero * numero
    lista_quadrados.append(numero_quadrado)
    
soma_quadrado= sum(lista_quadrados)
print(sum(lista_quadrados))