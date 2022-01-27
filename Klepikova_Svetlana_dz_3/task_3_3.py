def thesaurus(*args) -> dict:
    names = [*args]
    dict_out = {}
    for name in names:
        key = name[0]
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(name)
    return dict_out


print(thesaurus("Ариэль", "Люк", "Энекен", "Бэль", "Ксардас", "Диего", "Стрелок", "Шустрый", "Мононоке", "Кен", "Барби", "Аврора", "Коготь смерти", "Единорожка", "Луффи", "Нео"))


my_dict = {'А': ['Ариэль', 'Аврора'], 'Л': ['Люк', 'Луффи'], 'Э': ['Энекен'], 'Б': ['Бэль', 'Барби'], 'К': ['Ксардас', 'Кен', 'Коготь смерти'], 'Д': ['Диего'], 'С': ['Стрелок'], 'Ш': ['Шустрый'], 'М': ['Мононоке'], 'Е': ['Единорожка'], 'Н': ['Нео']}
def sorting_by_keys(my_dict):
    '''Сортировка словаря по ключам'''
    keys = list(my_dict.keys())
    keys.sort()
    for key in keys:
         result = print(f'{key} : {my_dict[key]}')
    return result


print(sorting_by_keys(my_dict))
