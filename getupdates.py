import requests
from pprint import pprint
token = '1687972442:AAFTgtZXybvpDqsTddplgtzO9GHUuenLwKs'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
# print(r.url)
data = r.json()
# pprint(data)
for i in range(len(data)):
    updates = data['result'][i]['message']['from']['first_name']
    print(updates)