from requests import Request, Session
import json

while True:
  crypto = str(input("Enter BTC, ETH, or LTC: "))
  if crypto == "BTC":
    cryptoid = "1"
    crypto = "bitcoin"
    break
  elif crypto == "ETH":
    cryptoid = "1027"
    crypto = "ethereum"
    break
  elif crypto == "LTC":
    cryptoid = "2"
    crypto = "litecoin"
    break
    

def getCryptoPrice(coin):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
    'slug':coin,
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '',
  }

  session = Session()
  session.headers.update(headers)

  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  
  return data


price = getCryptoPrice(crypto)['data'][cryptoid]['quote']['USD']['price']

print("The price of " + crypto + " is currently $" + "{:.2f}".format(price) + ".")