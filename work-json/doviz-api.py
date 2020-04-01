import json
from urllib.request import urlopen

with urlopen("https://www.doviz.gen.tr/doviz_json.asp?version=1.0.4") as response:

    data = json.load(response)

# print(data)                           # exploring the json object
# for key in data:
#     print(key)

print("\n"+"{} itibari ile döviz kurları aşağıdaki gibidir:".format(data['songuncellenme']))
print("Dolar / TL: {}".format(data['dolar']))
print("Euro / TL: {}".format(data['euro']))
print("Dolar / Euro: {}".format(data['dolareuro']))
print("Euro / Dolar: {}".format(data['eurodolar']))
