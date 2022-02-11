import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(([A-Za-z])+([0-9\-_\+\.])*@([A-Za-z])+([0-9\-_\+\.])*[\.]{1,1}[A-Za-z]+)')
    try:
        if RE_MAIL.findall(email):
            res = re.split(r'@', email)
            username = res[0]
            domen = res[1]
            di = {username: domen} #делаем словарь из res
            return print(di)
    except ValueError as err:
        print(f'Неверный e-mail. Ошибка: {err}')

if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
    email_parse('SVETLANA.LVOVSKAYA@gmail.com')
