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
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'
    }
    for key in translate:
        if value == key:
            str_out = translate[key]
    return str_out


print(num_translate_adv("Three"))
print(num_translate_adv("Four"))
print(num_translate_adv("five"))