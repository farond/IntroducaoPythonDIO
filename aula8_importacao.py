from aula7_televisao import televisao
from aula7_calculadora1 import calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = calculadora(5,10)
    print(calculadora.soma())
    lista = ['cachorro','gato','elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras da lista: {}'.format(total_letras))
    print(teste())