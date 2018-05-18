from pyquery import PyQuery
import requests
import os
from collections import OrderedDict
import creds

## Get a API key at https://www.openexchangerates.org and put it into the right spot in creds.py

url = 'https://openexchangerates.org/api/latest.json?app_id=' + creds.access['apikey']

# Available currencies are at http://docs.openexchangerates.org/docs/supported-currencies
r = requests.get(url)
json = r.json()
rates = json["rates"]

currencies = (
    ('Euro*', 'EUR', ''),
    ('Australia', 'AUD', 'dollars'),
    ('Brazil', 'BRL', 'reals'),
    ('Britain', 'GBP', 'pounds'),
    ('Canada', 'CAD', 'dollars'),
    ('Chile', 'CLP', 'pesos'),
	('China', 'CNY', 'yuan'),
    ('Denmark', 'DKK', 'kroner'),
    ('Egypt', 'EGP', 'pounds'),
    ('Hong Kong', 'HKD', 'dollars'),
    ('India', 'INR', 'rupees'),
    ('Israel', 'ILS', 'shekels'),
    ('Jamaica', 'JMD', 'dollars'),
    ('Japan', 'JPY', 'yen'),
    ('Kenya', 'KES', 'shillings'),
    ('Mexico', 'MXN', 'pesos'),
    ('Norway', 'NOK', 'kroner'),
    ('S. Africa', 'ZAR', 'rand'),
    ('Sweden', 'SEK', 'kronor'),
    ('Switzerland', 'CHF', 'francs'),
    ('Turkey', 'TRY', 'liras')
)

print("\r\n")
print("$1 EQUALS ...\r\n")

for currency in currencies:
    country, abbreviation, denomination = currency
    print(country + "\t" + "{0:.2f}".format(rates[abbreviation]) + "\t" + denomination + "\r\n")
    
print("\r\n")
print("* Euro nations are Austria, Belgium, Cyprus, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, the Netherlands, Portugal, Slovakia, Slovenia and Spain.\r\n")
print("Source: OpenExchangeRates.org\r\n")

