## 7) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, 
# I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
#****************************************|
#|   Preço por tipo e faixa de consumo   |
#****************************************|
#| Tipo        | Faixa (kWh)   | Preço   |
#| Residencial | Até 500       | R$ 0,40 |
#|             | Acima de 500  | R$ 0,65 |

#| Comercial   | Até 1000      | R$ 0,55 |
#|             | Acima de 1000 | R$ 0,60 |

#| Industrial  | Até 5000      | R$ 0,55 |
#|             | Acima de 5000 | R$ 0,60 |

#Constantes para faixa de (KWH)
#-----------------------
at_500 = 0.40
acima_500 = 0.65
at_1000 = 0.55
acima_1000=0.60
at_5000= 0.55
acima_5000= 0.60
#-----------------------
preco_pagar = 0
quantidade = float(input("Informe a quantiade de KWH consumida:"))
tipo_instalacao = input("Informe o Tipo de instalacao:\nR para residências\nI para indústrias\nC para comércios\nDigite:")
#Função pra calcular o preço do negocio..
def calcula_preco(quantidade,tipo_instalacao):
    if tipo_instalacao == "R":
        if quantidade > 500:
            preco_pagar = acima_500
        else:
            preco_pagar = at_500
    elif tipo_instalacao == "C":
        if quantidade > 1000:
            preco_pagar = acima_1000
        else:
            preco_pagar = at_1000
    elif tipo_instalacao == "I":
        if quantidade > 5000:
            preco_pagar =  acima_5000
        else:
            preco_pagar = at_5000
    
    return preco_pagar
print("*****Preço a pagar*****")
print("RS %.f"%(quantidade * calcula_preco(quantidade,tipo_instalacao)))

