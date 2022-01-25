def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    translate = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    for key in translate:
        if value == key.capitalize():
            str_out = translate.setdefault(key).capitalize()
        else:
            if value == key:
                str_out = translate.setdefault(key)
    return str_out


print(num_translate_adv("Three"))
print(num_translate_adv("four"))
print(num_translate_adv("Five"))
print(num_translate_adv("файв"))