#2) Escreva um programa que leia três números e que imprima o maior e o menor
#Função para verificar o maior numero
def maior_numero(n1,n2,n3):
    maior = n1
    if (n2 > maior):
        maior = n2
    if (n3 > maior):
        maior = n3
    return maior
#Função pra verificar o menor numero
def menor_numero(n1,n2,n3):
    menor = n1
    if (n2 < menor):
        menor = n2
    if(n3 < menor):
        menor = n3
    return menor

n1= input("Informe o 1ª numero:")
n2= input("Informe o 2ª numero:")
n3= input("Informe o 3ª numero:")
maior = maior_numero(n1,n2,n3)
menor = menor_numero(n1,n2,n3)
print("O maior numero é",maior,"e o menor numero é:",menor)

