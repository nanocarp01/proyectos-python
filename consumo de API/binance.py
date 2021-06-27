import requests

print("SOLICITANDO INFORMACION DE BINANCE")
print("espere....") 

url =('https://api.binance.com/api/v3/ticker/price')

data = requests.get(url)

data=data.json()

cripto = input("Ingrese crypto: ")
for elements in data:
    if elements['symbol'] == cripto :
        print("Moneda: ", elements['symbol'])
        print("Precio: ", elements['price'])
        print("-----------")