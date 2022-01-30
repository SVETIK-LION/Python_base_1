import requests
from decimal import *


def currency_rates(code: str) -> Decimal:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text_list = response.text.split('Valute')  # Разделяем текст по валютам
    for val in text_list:
        if code.upper() in val:
            val_list = val.split('<')  # Разделям список валют на элементы-характеристики нужной валюты
    for i in range(len(val_list)):
        if 'Value' in val_list[i]:
            rate = Decimal(float(
                f'{val_list[i][6:8]}.{val_list[i][9:]}'))  # Убираем запятую, срезами добавляем значения валюты, конвертим в decimal
            break
    for j in range(len(val_list)):
        if 'Nominal' in val_list[j]:
            nominal = Decimal(float(val_list[j][8:])) # Вычленяем номинал
            break
    result_value = f'{rate / nominal} - точный курс валюты {code.upper()} по отношению к рублю' # Находим значение
    return result_value


print(currency_rates("usd"))
print(currency_rates("AZN"))
print(currency_rates("Amd"))
print(currency_rates("HUF"))
print(currency_rates("noname"))
