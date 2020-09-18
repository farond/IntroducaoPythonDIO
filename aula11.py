
lista = [1,10]
try:
    divisao = 10 / 0
    numero = lista[1]
except ZeroDivisionError:
    print('Nao é possível realizar uma divisão por 0')
