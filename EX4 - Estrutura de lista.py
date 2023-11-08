# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.

lista_caract= []

print('Digite 10 caracteres, para verificar quais são consoantes')
for i in range(10):
    caract= input(f'Digite o {i+1} caracter: ')
    caract= caract.upper()
    lista_caract.append(caract)
    
for i, consoante in enumerate(lista_caract):
    if consoante == 'A' or consoante =='E' or consoante == 'I' or consoante == 'O' or consoante == 'U':
        print(f'{consoante} É uma vogal')
    else:
        print(f'{consoante} É uma consoante')