from ast import Lambda, main
from requests import Request, Session
from tkinter import *
import json

root = Tk()
root.title("Live Price of Cryptocurrency")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def getCryptoPrice(coin, cryptoid):
  e.delete(0, END)

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
  
  price = data['data'][cryptoid]['quote']['USD']['price']

  e.insert(0, "$" + "{:.2f}".format(price))
  return



b1 = Button(root, text="BTC", padx=40, pady=20, command=lambda: getCryptoPrice("bitcoin", "1"))
b2 = Button(root, text="ETH", padx=40, pady=20, command=lambda: getCryptoPrice("ethereum", "1027"))
b3 = Button(root, text="LTC", padx=40, pady=20, command=lambda: getCryptoPrice("litecoin", "2"))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

root.mainloop()