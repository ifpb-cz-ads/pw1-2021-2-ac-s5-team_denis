##4) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens 
# mais longas.
viagem_curta=0.5
viagem_longe=0.45
preco_passagem = 0
distancia = float(input("Informe o valor da distancia em km:"))
#Função para calcular o preço da passagem
def calcula_preco(valor):
    if (distancia > 200):
        valor = distancia * viagem_curta
    else:
        valor = distancia * viagem_longe
    return valor

print("O preço da passagem será:",calcula_preco(distancia))
    