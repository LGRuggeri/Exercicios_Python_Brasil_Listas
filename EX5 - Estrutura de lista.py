# 5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista_par= []
lista_impar= []

print('Digite 20 inteiros, para serem separados por PAR e IMPAR')
for i in range(20):
    numeros= int(input(f'Digite o {i+1} número inteiro: '))
    if numeros%2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

print('Os números inteiros pares são: ', lista_par)
print('Os números impares são: ', lista_impar)