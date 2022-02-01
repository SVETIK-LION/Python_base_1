import requests
from decimal import *


def currency_rates(code: str) -> Decimal:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text_list = response.text.split('<Valute ID=')  # Разделяем текст по валютам
    for value in text_list:
        if code.upper() in value:
            val = value.replace('</Value>', '<Value>') # Меняем ненужные строчки, чтобы по ним сделть сплит
            val = val.split('<Value>') # Разделяем по строке курса валюты
            val = Decimal(val[-2].replace(',', '.')) # Меняем точку на зпт в значении курса валюты
            nom = value.replace('</Nominal', '<Nominal>') # То же самое только для номинала
            nom = nom.split('<Nominal>')
            nom = Decimal(nom[-2])
            val_out = val/nom # Делим курс на номинал
            return f'{val_out} точный курс валюты {code.upper()} по отношению к рублю'


print(currency_rates("USD"))
print(currency_rates("AZN"))
print(currency_rates("Amd"))
print(currency_rates("HUF"))
print(currency_rates("noname"))
