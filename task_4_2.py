import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    result_value = 1.11  ## здесь должно оказаться результирующее значение float
    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))