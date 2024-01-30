from datetime import datetime

data_now = datetime.now()
print(data_now.timestamp())

print(datetime.fromtimestamp(data_now.timestamp()))

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('04/06/1990 19:00:00', fmt)
data_atual = datetime.strptime('30/01/2024 10:41:00', fmt)
print(data_atual - data_inicio)