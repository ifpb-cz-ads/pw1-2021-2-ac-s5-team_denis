##6) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
valor_casa = float(input("Informe o valor da casa:"))
valor_salario = float(input("Informe o valor do seu humilde salario:"))
quantidade_anos=  float(input("Informe a quantidade de anos a pagar: "))
meses = quantidade_anos*12
prestacao = valor_casa / meses
if  prestacao > valor_salario * 0.30:
    print("Emprestimo não aprovado, você dançou")
else:
    print("Emprestimo aprovado, parabéns!!!")


