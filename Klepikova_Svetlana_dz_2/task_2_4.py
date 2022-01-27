def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    for i in range(len(list_in)):
        list_in[i] = list_in[i].title().split()
        list_in[i] = f"Привет, {list_in[i][-1]}!"
    list_out = list_in
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
