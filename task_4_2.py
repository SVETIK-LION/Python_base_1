import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    payload = {'code: value'}
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    result_value = r.url  ## здесь должно оказаться результирующее значение float
    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))