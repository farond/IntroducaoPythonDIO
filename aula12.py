import requests

response = requests.get('http://viacep.com.br/ws/22041001/json/')
print(response.status_code)
print(response.text)
print(response.json())
dados_cep = response.json()
print(dados_cep['logradouro'])
print(dados_cep['complemento'])