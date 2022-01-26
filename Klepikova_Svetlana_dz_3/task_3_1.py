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
    if value.istitle():
        return translate.get(value.lower()).capitalize()
    else:
        return translate.get(value)


print(num_translate_adv("Three"))
print(num_translate_adv("four"))
print(num_translate_adv("Five"))
print(num_translate_adv("файв"))
