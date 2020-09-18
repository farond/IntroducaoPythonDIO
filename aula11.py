
# lista = [1,10]
# try:
#     divisao = 10 / 0
#     numero = lista[1]
# except ZeroDivisionError:
#     print('Nao é possível realizar uma divisão por 0')

# lista = [1,10]
# try:
#     divisao = 10 / 1
#     numero = lista[3]
#
# except ZeroDivisionError:
#     print('Nao é possível realizar uma divisão por 0')
# except IndexError:
#     # print('Erro ao acessar um indice inválido da lista')

lista = [1, 10]
arquivo = open ('test.text', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    #divisao = 10 / 0
    numero = lista[1]
    #x = a

#funcionamento em arvore
except ZeroDivisionError:
    print('Nao é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação Aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex: #Pai de todas as except
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando não ocorre exceção')

finally: #dando erro ou não, irá executar o que está dentro dele
    print('Sempre executa')
    print('Arquivo fechado')
    arquivo.close()

try:
  x = 1
  elementos = ['terra', 'ar', 'fogo', 'agua']
  elementos.pop(x)
except:
  print('Elemento não encontrado')
else:
  print('Elemento {} removido.'.format(x))
finally:
  print('Busca completa')




