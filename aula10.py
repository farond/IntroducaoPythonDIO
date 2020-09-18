from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    #print(data_atual.day)
    #print(data_atual.year)
    #print(data_atual.hour)
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(1995, 6, 28, 13, 15, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S') #converte para String
    print(type(data_convertida))
    print(data_convertida)
    nova_data_sub = data_convertida - timedelta(days=365, hours=2, minutes=25, seconds=3600)
    nova_data_ad = data_convertida + timedelta(days=365, hours=2, minutes=25, seconds=3600)
    print(nova_data_sub)
    print(nova_data_ad)
    data_atual = datetime.now()
    resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(resultado)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print((type(data_atual)))
    print(data_atual_str)
    #print(data_atual.strftime('%d/%m/%y') )
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15 , minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str)) #String

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
