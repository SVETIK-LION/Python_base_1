def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    result_list = []
    for element in list_in:
        if element[0] in ['+', '-'] or element.isdigit():
            if element.isdigit():
                result_list.append(f'"{element.zfill(2)}"')
            else:
                result_list.append(f'"{element[0]} {element[1:].zfill(2)}"')
        else:
            result_list.append(element)
    str_out = ' '.join((result_list))
    return str_out


my_list = ['в', '15', 'часов', '25', 'минут', 'температура', 'воздуха', 'была', '-17', 'градусов']
result = convert_list_in_str(my_list)
print(result)
