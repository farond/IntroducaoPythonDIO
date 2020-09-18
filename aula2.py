# a = 10
# b = 5

a= int(input("Entre com o primeiro valor: "))
b= int(input("Entre com o segundo valor: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print("Soma: {}. Subtração: {}".format(soma, subtracao))

resultado = ("Soma: {soma}. \nSubtração: {sub}. "
      "\nMultiplicação: {mult}."
      "\nDivisão: {div}."
      "\nResto: {resto}".format(soma= soma, sub=subtracao, mult= multiplicacao, div=divisao, resto=resto))

print(resultado)

# print("Soma: " + str(soma))
# print("Subtração: " + str(subtracao))
# print(multiplicacao)
# print(int(divisao))
# print(divisao)
# print(resto)

# x = "1"
# soma2 = int(x) + 1
# print(soma2)