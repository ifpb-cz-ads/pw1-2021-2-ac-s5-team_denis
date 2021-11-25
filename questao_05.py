##5) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada
resultado = 0
n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))
operacao = input("informe a operação ex: (+) (-) (*) (/) : ")
if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "/":
    resultado = n1 / n2
elif operacao == "*":
    resultado = n1 * n2
else:
    print("*********operação invalida**********")
print("****RESULTADO****\n")    
print(resultado)