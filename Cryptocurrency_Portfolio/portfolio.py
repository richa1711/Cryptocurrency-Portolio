# we will use the quote end point for acquiring the specific info about the
# cryptocurrencies we have enlisted in excel

import os
import csv
import json
# json is the structure of the text that we pull from the api.
import requests
#for making api requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = 'RUP'
local_symbol = '₹'

api_key = 'ENTER_YOUR_OWN_API_KEY_;)'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("My Portfolio")
print()

portfolio_value = 0.00
#Basic table setup to specify rowname
table = PrettyTable(['Asset', 'Amount Owned', 'Value', 'Price', '1h', '24h', '7d'])
# letter "r" says we want to open the excel in read only mode
with open("my_portfolio.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if '\ufeff' in line[0]:
            line[0] = line[0][1:].upper()
        else:
            line[0] = line[0].upper()

        amount = line[1]
        symbol = line[0]

# now we will make the api call
        quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol
        request = requests.get(quote_url, headers = headers)
        results = request.json()

        # print(json.dumps(results, sort_keys=True, indent=4))

        currency = results['data'][symbol]
        name = currency['name']
        quote = currency['quote'][local_currency]
        hour_change = round(quote['percent_change_1h'],2)
        day_change = round(quote['percent_change_24h'],2)
        week_change = round(quote['percent_change_7d'],2)

        price = quote['price']

        value = float(price) * float(amount)

        portfolio_value += value

        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL


        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL


        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        price_string = '{:,}'.format(round(price,2))
        value_string = '{:,}'.format(round(value,2))

        table.add_row([f"{name} ({symbol})",
                        amount,
                        local_symbol+value_string,
                        local_symbol+price_string,
                        str(hour_change),
                        str(day_change),
                        str(week_change)])


print()
print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
print(f"Total Portfolio Value: {Back.GREEN}{local_symbol}{portfolio_value_string}{Style.RESET_ALL}")
print()
