import requests
from pprint import pprint
token = '1602686596:AAFiy3eteVMwvKw8RT-PU8xgZLlzHqemCK0'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
# print(r.url)
data = r.json()
# pprint(data)
for i in range(len(data['result'])):
    f_name=data['result'][i]['message']['from'].get('first_name','')
    l_name=data['result'][i]['message']['from'].get('last_name','')
    updates =f'{f_name} {l_name}'
    pprint(updates)