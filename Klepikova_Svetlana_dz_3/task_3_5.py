from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    for _ in range(count):
        word_1, word_2, word_3 = choice(nouns), choice(adverbs), choice(adjectives)
        joke = f'{word_1} {word_2} {word_3}'
        list_out.append(joke)
    return list_out


print(get_jokes(2))
print(get_jokes(10))


#Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, repeat=True) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    if repeat == False:
        min_count = min(len(nouns), len(adverbs), len(adjectives))
        if count > min_count:
            count = min_count
    for _ in range(count):
        word_1, word_2, word_3 = choice(nouns), choice(adverbs), choice(adjectives)
        if repeat == False:
            nouns.remove(word_1)
            adverbs.remove(word_2)
            adjectives.remove(word_3)
        joke = f'{word_1} {word_2} {word_3}'
        list_out.append(joke)
    return list_out


print(get_jokes_adv(count=10, repeat=False))
