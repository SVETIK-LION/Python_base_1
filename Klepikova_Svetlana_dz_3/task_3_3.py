def thesaurus(*args) -> dict:
    names = [*args]
    dict_out = {}
    for name in names:
        key = name[0]
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(name)
    return dict_out


print(thesaurus("Ариэль", "Люк", "Бэль", "Ксардас", "Диего", "Стрелок", "Шустрый", "Мононоке", "Кен", "Барби", "Аврора", "Коготь смерти", "Единорожка", "Луффи", "Нео"))