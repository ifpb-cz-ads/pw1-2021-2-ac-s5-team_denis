##3) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.
def calcula_aumento(valor=float):
    if (valor > 1250):
        valor = valor * 1.10#Aumento de 10%
    else:
        valor = valor * 1.15#Aumento de 15%
    return valor
salario = float(input("Informe o salário do funcionário:"))
aumento = calcula_aumento(salario) - salario
print("Antigo Sálario:",salario)
print("Aumento de ",aumento)
print("Novo Salário:",calcula_aumento(salario))
