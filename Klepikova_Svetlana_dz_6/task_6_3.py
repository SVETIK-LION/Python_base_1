import sys
import json
from itertools import zip_longest


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    list_users = []
    list_hobby = []
    count_key = 0
    count_val = 0
    users_file = open('users.csv', 'r', encoding='utf-8')
    for line_u in users_file:
        key = line_u.strip().replace(',', ' ')
        list_users.append(key)
        count_key += 1
    hobby_file = open('hobby.csv', 'r', encoding='utf-8')
    for line_h in hobby_file:
        val = line_h.strip()
        list_hobby.append(val)
        count_val += 1
    if count_key < count_val:
        return 1
    else:
        return {key: val for key, val in zip_longest(list_users, list_hobby)} # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
print(dict_out) # Вывожу словарь или единицу (если имен меньше, чем хобби)
