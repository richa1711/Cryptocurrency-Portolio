#....... For Accessing the data of some selected currencies in detal we use quotes endpoint
# The user can add ticker symbol of currencies and can fetch the current market data
import requests
import json

local_currency = 'RUP'
local_symbol = '₹'
api_key = 'ENTER_YOUR_OWN_API_KEY_;)'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'
symbol = input('Enter the ticker symbol of a cryptocurrency: ')
# THE USER MIGHT CAN INPUT LETS SAY BTC for acquiring bitcoin market value info
global_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency +'&symbol='+symbol

request = requests.get(global_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))
data = results["data"]
# for extracting price , %change in 24h, market cap of all the existing cryptocurrencies
# from json

currency = data[symbol]
name = currency['name']

price = currency['quote'][local_currency]['price']
percent_change_24h = currency['quote'][local_currency]['percent_change_24h']
market_cap = currency['quote'][local_currency]['market_cap']

price = round(price,2)
percent_change_24h = round(percent_change_24h,2)
market_cap = round(market_cap,2)

price_string = local_symbol + '{:,}'.format(price)
percent_change_24_string = local_symbol + '{:,}'.format(percent_change_24h)
market_cap_string = local_symbol + '{:,}'.format(market_cap)

print(f"{name} ({symbol})")
print(f"Price: {price_string}")
print(f"24h Change: {percent_change_24_string}")
print(f"Market Cap: {market_cap_string}")
print()
