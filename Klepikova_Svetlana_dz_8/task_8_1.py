import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^([A-Za-z0-9]{1}[A-Za-z0-9\-_\+\.]+[A-Za-z0-9]{1})@([A-Za-z0-9]+\.){1,2}[A-Za-z]{2,}$')
    try:
        if RE_MAIL.findall(email):
            res = re.split(r'@', email)
            user = res[0]
            domen = res[1]
            di = {'username': user, 'domain': domen}
            return di.copy()
        else:
            raise ValueError(f'Wrong email: {email}')
    except ValueError as err:
        return err

if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
    print(email_parse('SVETLANA.LVOVSKAYA@gmail.com'))
    print(email_parse('Svetik-Lion@po4ta.ru'))
    print(email_parse('wrong.e-mail@@mail.com'))
    print(email_parse('po4ta_01234@n7.si.com'))
    print(email_parse('Mikkey-Mouse@mail..com'))
