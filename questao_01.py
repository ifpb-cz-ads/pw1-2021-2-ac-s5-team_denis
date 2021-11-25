##1) Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
multa_km = 5
velocidade_carro = float(input("Informe a velocidade do carro:"))
    
#Função pra verificar a velocidade do carro
def velocidade(velocidade):
    if velocidade > 80:
        return True;
    else:
        return False;
        
v = velocidade(velocidade_carro)
if  (v == True):
    print("Você foi multado em: R$",velocidade_carro*multa_km)
else:
    print("Ta de boa pode ir...")