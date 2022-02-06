from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    list_all = list()
    list_all.append(line)
    for i in range(len(list_all)):
        tuple_line = (list_all[i][0], list_all[i][5].replace('"', ''), list_all[i][6])
    return tuple_line # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for val in fr.readlines():
        line = val.split(' ')
        list_out.append(get_parse_attrs(line))# передавайте данные в функцию и наполняйте список list_out кортежами

pprint(list_out)
