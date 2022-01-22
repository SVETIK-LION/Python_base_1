def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    res = []
    for i in range(len(list_in)):
        list_in[i] = list_in[i].title().split()
        res.append(list_in[i][-1])
    for j in range(len(res)):
        res[j] = f'Привет, {res[j]}!'
    list_out = res
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)