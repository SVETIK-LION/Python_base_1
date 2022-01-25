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
        if value.istitle():
            if value == key.capitalize():
                str_out = translate[key].capitalize()
        else:
            if value == key:
                str_out = translate[key].lower()
    return str_out


print(num_translate_adv("three"))
print(num_translate_adv("Four"))
print(num_translate_adv("Five"))