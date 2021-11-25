##4) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens 
# mais longas.
viagem_curta=0.5
viagem_longe=0.45
preco_passagem = 0
distancia = float(input("Informe o valor da distancia em km:"))
if (distancia > 200):
    preco_passagem = distancia * viagem_curta
else:
    preco_passagem = distancia * viagem_longe
    
print("O preço da passagem será:",preco_passagem)
    