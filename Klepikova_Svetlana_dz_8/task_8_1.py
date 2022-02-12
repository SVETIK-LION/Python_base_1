import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(([A-Za-z0-9])+([A-Za-z0-9\-_\+\.][A-Za-z0-9])*@([A-Za-z0-9])+([0-9\-_\+\.])*[\.]{1}[A-Za-z]+)')
    try:
        if RE_MAIL.findall(email):
            res = re.split(r'@', email)
            username = res[0]
            domen = res[1]
            di = {username: domen} #делаем словарь из res
            return print(di)
        else:
            raise ValueError
    except ValueError as err:
        print(f'Неверный e-mail')

if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
    email_parse('SVETLANA.LVOVSKAYA@gmail.com')
    email_parse('Svetik-Lion@po4ta.ru')
    email_parse('wrong.e-mail@@mail..com')
    email_parse('po4ta01234@n_7.com')

