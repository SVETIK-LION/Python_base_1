import requests
from decimal import *


def currency_rates(code: str) -> Decimal:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text_list = response.text.split('<Valute ID=')  # Разделяем текст по валютам
    for value in text_list:
        if code.upper() in value:
            # Меняем ненужные строчки, чтобы по ним сделть сплит, делаем сплит, меняем тчк на зпт, преобразуем в Decimal
            val = Decimal(value.replace('</Value>', '<Value>').split('<Value>')[-2].replace(',', '.'))
            # То же самое, только для номинала
            nom = Decimal(value.replace('</Nominal', '<Nominal>').split('<Nominal>')[-2])
            val_out = val/nom # Делим курс на номинал
            return f'{val_out} точный курс валюты {code.upper()} по отношению к рублю'

if __name__ == "__main__":
    currency_rates(code)