import requests
# URL = f"https://www.cbr-xml-daily.ru/daily_json.js"
# r= requests.get(url=URL)
# result = r.json()
#
# #статус 200 это успешно
# if r.status_code==200:
#     print(result)
#     print(type(result))
#     print(r.status_code)
#
# else:
#     print('Nope')



API_KEY = "4c4d49ca61-f53c040c2f-t10b8y"  # твой ключ
curr = "CNY"
URL = f"https://v6.exchangerate-api.com/v6/4c4d49ca61-f53c040c2f-t10b8y/latest/USD"

r = requests.get(URL)
data = r.json()

print(data)  # <-- смотри, что вернёт
