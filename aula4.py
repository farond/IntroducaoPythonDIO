a = int(input("Primeiro bimestre: "))
while a > 10:
    a = int(input("Você digitou errado. Primeiro Bimestre: "))
b = int(input("Segundo bimetre: "))
while b > 10:
    b = int(input("Você digitou errado. Segundo Bimestre: "))
c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input("Você digitou errado. Terceiro Bimestre: "))
d = int(input("Quarto bimetre: "))
while d > 10:
    d = int(input("Você digitou errado. Qaurto Bimestre: "))

media = (a + b + c + d) / 4
print("media: {}".format(media))

if media < 7:
    print("Aluno reprovado")
else:
    print("Aluno aprovado")

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota: '))
# print (nota)
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Entre com um valor: '))
# for num in range (a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print ((num))

# a = int(input("Entre com o número: "))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print ("Numero {} é primo".format(a))
# else:
#     print("Numero {} não é primo".format(a))